from django.urls import path
from .views import *

urlpatterns=[
    path('add_to_cart/<int:pk>',add_to_cart,name='add_to_cart'),
    path('cart_item/',cart_item,name='cart_item'),
    path('addItem/<int:id>',addItem,name='addItem'),
    path('removeItem/<int:id>',removeItem,name='removeItem'),
    path('delItem/<int:id>',delItem,name='delItem'),
]