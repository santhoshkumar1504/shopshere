from django.urls import path
from .views import *

urlpatterns=[
    path('',home,name='home'),
    path('productDetail/<int:id>',productDetail,name='productDetail'),
    path('about/',about,name='about')
]