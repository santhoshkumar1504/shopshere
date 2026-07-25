from django.db import models
from django.contrib.auth.models import User
from product.models import ProductModel

class AddressModel(models.Model):
    host=models.ForeignKey(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    phone_no =models.CharField(max_length=13)
    email=models.EmailField()
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pinCode=models.CharField(max_length=6)
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)



class OrderModel(models.Model):
    Status_Choices=(
        ('Pending','Pending'),
        ('Confirmed','Confirmed'),
        ('Shipped','Shipped'),
        ('Delivered','Delivered'),
        ('Cancelled','Cancelled')
    )        
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.ForeignKey(AddressModel,on_delete=models.CASCADE)
    total_amt=models.DecimalField(max_digits=10,decimal_places=2)
    status=models.CharField(max_length=50,choices=Status_Choices,default='Pending')
    created_at=models.DateTimeField(auto_now_add=True)



class OrderItemModel(models.Model):
    order=models.ForeignKey(OrderModel,on_delete=models.CASCADE)
    product=models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.IntegerField()

