from django.urls import path
from .views import *

urlpatterns=[
    path('',login_,name='login_'),
    path('logout/',logout_,name='logout_'),
    path('register/',register,name='register'),
    path('forgetPasw/',forgetPasw,name='forgetPasw'),

    # User Profile
    path('profile/',profile,name='profile'),
    path('updateProfile/',updateProfile,name='updateProfile'),
    path('completeProfile/',completeProfile,name='completeProfile'),
    path('deleteProfile/',deleteProfile,name='deleteProfile'),
    path('resetPasw/',resetPasw,name='resetPasw')
]