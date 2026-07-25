from django.shortcuts import render
from product.models import ProductModel, CategoryModel

def home(request):
    if 'q' in request.GET:
        q=request.GET['q']
        data=ProductModel.objects.filter(is_delete=False,pname__icontains=q,stock__gt=0).order_by('?')

    elif 'category' in request.GET:
        cname=request.GET['category']
        cat=CategoryModel.objects.get(cname__icontains=cname)
        data=ProductModel.objects.filter(category=cat.id,is_delete=False,stock__gt=0).order_by('?')

    else:
        data=ProductModel.objects.filter(is_delete=False,stock__gt=0).order_by('?')

    Category=[]
    category=CategoryModel.objects.filter(is_deleted=False)
    for i in category:
        if i.cname not in Category:
            Category.append(i.cname)

    return render(request,'home.html',{'data':data,'category':Category})



def productDetail(request,id):
    product=ProductModel.objects.get(id=id)
    related_product=ProductModel.objects.filter(category=product.category).exclude(id=id).order_by('?')[:4]
    return render(request,'productDetail.html',{'product':product,'related_product':related_product})




def about(request):
    return render(request,'about.html')

# display details

# <a href="?category=Shoes">SHoes</a>
# print(type(cname)) string

