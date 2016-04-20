from django.contrib import admin

from main.models import Farm, Product, Basket, ShoppingItem, Provider

# Register your models here.
# admin.site.register(Provider)
# admin.site.register(Farm)
# admin.site.register(Product)
# admin.site.register(Basket)
# admin.site.register(ShoppingItem)


@admin.register(Provider)
class AdminProvider(admin.ModelAdmin):
        list_display = ('user','certificado',)
        List_Filter = ('user',)

@admin.register(Farm)
class AdminFarm(admin.ModelAdmin):
        list_display = ('name', 'latitude','longitude','size','provider',)
        List_Filter = ('name',)

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
        list_display = ('name', 'price','unit_value','unit_name','farm','description','quantity')
        List_Filter = ('name',)

@admin.register(Basket)
class AdminBasket(admin.ModelAdmin):
        list_display = ('name', 'start_date','end_date',)
        List_Filter = ('name',)

@admin.register(ShoppingItem)
class AdminShoppingItem(admin.ModelAdmin):
        list_display = ('quantity', 'user','product', 'basket', 'state', 'session', 'create_date',)
        List_Filter = ('state', 'user', 'product', 'basket',)
