from django.shortcuts import render, redirect,get_object_or_404
from .forms import AddressForm
from cart.models import CartModel
from product.models import ProductModel
from .models import AddressModel, OrderModel, OrderItemModel
from django.contrib.auth.decorators import login_required
from django.contrib import messages



@login_required(login_url='login_')
def address(request):
    detail=AddressModel.objects.filter(host_id=request.user.id)
    return render(request,'address.html',{'detail':detail})

@login_required(login_url='login_')
def addAddress(request):
    form=AddressForm()
    if request.method=='POST':
        form_data=AddressForm(request.POST)
        if form_data.is_valid():
            obj=form_data.save(commit=False)
            obj.host_id=request.user.id

            if obj.is_default:
                addr=AddressModel.objects.filter(host=request.user)
                for i in addr:
                    i.is_default=False
                    i.save()
                obj.save()
                return redirect(address)
            else:
                obj.save()
                return redirect(address)
            
    return render(request,'addaddress.html',{'form':form})




@login_required(login_url='login_')
def updateAddress(request,id):
    model_data=AddressModel.objects.get(id=id)
    form=AddressForm(instance=model_data)
    if request.method=='POST':
        formdata=AddressForm(request.POST,instance=model_data)
        if formdata.is_valid():
            obj=formdata.save(commit=False)

            if obj.is_default:
                addr=AddressModel.objects.filter(host=request.user)
                for i in addr:
                    i.is_default=False
                    i.save()
                obj.save()
                return redirect(address)
            else:
                obj.host_id=request.user.id
                obj.save()
                return redirect(address)
            
    return render(request,'updateaddress.html',{'form':form})





@login_required(login_url='login_')
def deleteAddress(request,id):
    AddressModel.objects.get(id=id).delete()
    return redirect(address)



# Checkout Page views----------------------------------------------------------

@login_required(login_url='login_')
def checkout(request):
    addr=AddressModel.objects.filter(host=request.user, is_default=True).first()
    if not addr:
        addr=AddressModel.objects.filter(host=request.user).order_by('-created_at').first()

    all_address=AddressModel.objects.filter(host=request.user)
    items=CartModel.objects.filter(host=request.user)
    grand_total=sum(i.total_price for i in items)
    return render(request,'checkout.html',{'items':items,'addr':addr,'grand_total':grand_total,'all_address':all_address,'addr':addr})



@login_required(login_url='login_')
def caddItem(request,id):
    item=get_object_or_404(CartModel,id=id)
    if item.quantity>=item.product.stock:
        messages.error(request,'Number of Stock Unavailable')
        return redirect(checkout)
    else:
        item.quantity+=1
        item.save()
    return redirect(checkout)


@login_required(login_url='login_')
def cremoveItem(request,id):
    item=get_object_or_404(CartModel,id=id)
    if item.quantity==1:
        return redirect(checkout)
    else:
        item.quantity-=1
        item.save()
        return redirect(checkout)


@login_required(login_url='login_')
def cdelItem(request,id):
    CartModel.objects.get(id=id).delete()
    return redirect(checkout)




@login_required(login_url='login_')
def placeorder(request):
    if request.method=='POST':
        addre=AddressModel.objects.get(id=request.POST['curraddr'])
        total_amt=request.POST['total']

        orders=OrderModel.objects.create(
            address=addre,
            user=request.user,
            total_amt=total_amt  
        )

        items=CartModel.objects.filter(host=request.user)

        for item in items:
            OrderItemModel.objects.create(
                order=orders,
                product=item.product,
                price=item.total_price,                    
                quantity=item.quantity
            )
            orders.status='Confirmed'
            orders.save()

            ptd=ProductModel.objects.get(id=item.product.id)
            ptd.stock-=item.quantity
            ptd.save()
            item.save()
        
        CartModel.objects.filter(host=request.user).delete()
        return redirect(ordersuccess,orders.id)
        
    return redirect('cart_item')


@login_required(login_url='login_')
def ordersuccess(request,id):
    order=OrderModel.objects.get(id=id)
    return render(request,'success.html',{'order':order})



@login_required(login_url='login_')
def orders(request):
    ordered=OrderItemModel.objects.filter(order__user=request.user)
    return render(request,'order.html',{'ordered':ordered})



@login_required(login_url='login_')
def cancelorder(request,id):
    OrderItemModel.objects.get(id=id).delete()
    return redirect(orders)