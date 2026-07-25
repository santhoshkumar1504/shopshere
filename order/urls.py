from django.urls import path
from .views import *

urlpatterns=[
    path('address/',address,name='address'),
    path('addaddress/',addAddress,name='addaddress'),
    path('updateAddress/<int:id>',updateAddress,name='updateAddress'),
    path('deleteAddress/<int:id>',deleteAddress,name='deleteAddress'),

    path('checkout/',checkout,name='checkout'),
    path('caddItem/<int:id>',caddItem,name='caddItem'),
    path('cremoveItem/<int:id>',cremoveItem,name='cremoveItem'),
    path('cdelItem/<int:id>',cdelItem,name='cdelItem'),

    path('placeorder/',placeorder,name='placeorder'),
    path('',orders,name='orders'),
    path('ordersuccess/<int:id>',ordersuccess,name='ordersuccess'),
    path('cancelorder/<int:id>',cancelorder,name='cancelorder')
]