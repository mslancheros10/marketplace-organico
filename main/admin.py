from django.contrib import admin

from main.models import Farm, Product, Basket, ShoppingItem, Provider

# Register your models here.
admin.site.register(Provider)
admin.site.register(Farm)
admin.site.register(Product)
admin.site.register(Basket)
admin.site.register(ShoppingItem)