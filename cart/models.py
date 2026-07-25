from django.db import models
from product.models import ProductModel
from django.contrib.auth.models import User

class CartModel(models.Model):
    product=models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    host=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateField(auto_now_add=True)
    is_delete=models.BooleanField(default=False)

    @property
    def total_price(self):
        return self.product.price * self.quantity

    class Meta:
        unique_together=['host','product']

    