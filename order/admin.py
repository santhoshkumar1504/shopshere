from django.contrib import admin
from .models import OrderModel, OrderItemModel, AddressModel

class OrderAdmin(admin.ModelAdmin):
    list_display=['id','user','address','total_amt','status','created_at']
    list_display_links=['user']
    search_fields=['user']
    readonly_fields=['address','user']

class OrderItemAdmin(admin.ModelAdmin):
    list_display=['id','order','product','price','quantity']

admin.site.register(OrderItemModel,OrderItemAdmin)
admin.site.register(OrderModel,OrderAdmin)