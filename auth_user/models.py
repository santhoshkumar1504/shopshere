from django.db import models
from django.contrib.auth.models import User

class UserDetails(models.Model):
    address=models.TextField(max_length=100,null=True)
    pincode=models.IntegerField(null=True)
    phone=models.CharField(max_length=10)
    pic=models.ImageField(upload_to='users/',default='default.jpg')
    userId=models.ForeignKey(User,on_delete=models.CASCADE)