from django.shortcuts import render, redirect, get_object_or_404
from product.models import ProductModel
from .models import CartModel
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='login_')
def add_to_cart(request,pk):
    product=ProductModel.objects.get(id=pk)
    try:
        CartModel.objects.create(
            host=request.user,
            product=product
        )
    except:
        c=CartModel.objects.get(product=product,host=request.user)
        c.quantity=c.quantity+1
        c.save()
    return redirect('home')



@login_required(login_url='login_')
def cart_item(request):
    cartdata=CartModel.objects.filter(host=request.user)
    grand_total=sum(i.total_price for i in cartdata)
    total_items=sum(i.quantity for i in cartdata)
    return render(request,'cartItem.html',{'cartdata':cartdata,'grand_total':grand_total,'total_items':total_items})



@login_required(login_url='login_')
def addItem(request,id):
    item=get_object_or_404(CartModel,id=id)
    item.product.price=(item.quantity+1)*item.product.price
    if item.quantity>=item.product.stock:
        messages.error(request,'No. of stock unavaible')
    else:
        item.quantity+=1
        item.save()
    return redirect(cart_item)



@login_required(login_url='login_')
def removeItem(request,id):
    item=get_object_or_404(CartModel,id=id)
    if(item.quantity==1):
        return redirect(cart_item)
    else:
        item.product.price=(item.quantity-1)*item.product.price
        item.quantity-=1
        item.save()
    return redirect(cart_item)




@login_required(login_url='login_')
def delItem(request,id):
    CartModel.objects.get(id=id).delete()
    return redirect(cart_item)