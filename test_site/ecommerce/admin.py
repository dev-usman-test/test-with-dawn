from django.contrib import admin
from ecommerce.models import Product
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'image', )

admin.site.register(Product, ProductAdmin)
