from django.db import models

class CategoryModel(models.Model):
    cname=models.CharField(max_length=50,unique=True)
    cimg=models.ImageField(upload_to='category/',default='default.jpg',blank=True,null=True)
    is_deleted=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.cname


class ProductModel(models.Model):
    category=models.ForeignKey(CategoryModel,on_delete=models.CASCADE)
    pname=models.CharField(max_length=50)
    pdesc=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField(default=0)
    is_available=models.BooleanField(default=False)
    pimage=models.ImageField(upload_to='products/',default='default.jpg')
    is_delete=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

    