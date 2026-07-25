from django.contrib import admin
from .models import ProductModel, CategoryModel


class ProductAdmin(admin.ModelAdmin):
    model=ProductModel
    list_display=['pname','price','category','stock','is_available','created_at']
    search_fields=['pname','category']
    list_filter=['stock','price']
    list_per_page=10
    
admin.site.register(ProductModel,ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    model=CategoryModel
    list_display=['cname','cimg','is_deleted','created_at']

admin.site.register(CategoryModel,CategoryAdmin)