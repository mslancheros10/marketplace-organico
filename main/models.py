from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Provider(models.Model):
    user = models.OneToOneField(User,null=True)
    certificado = models.BooleanField(default=False)

class Farm(models.Model):
    name = models.CharField(max_length=100,blank=True)
    latitude = models.CharField(max_length=100,blank=True)
    longitude = models.CharField(max_length=100,blank=True)
    size = models.CharField(max_length=100,blank=True) # 5 hectareas
    provider = models.ForeignKey(Provider,null=True)

class Product(models.Model):
    name = models.CharField(max_length=100,blank=True)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    image_url = models.CharField(max_length=1000,blank=True)
    unit_value = models.CharField(max_length=100,blank=True)
    unit_name = models.CharField(max_length=100,blank=True)
    farm = models.ForeignKey(Farm,null=True)
    description = models.CharField(max_length=200,blank=True)
    quantity = models.IntegerField(blank=True,null=True)

class Basket(models.Model):
    name = models.CharField(max_length=100,blank=True)
    start_date = models.DateTimeField(blank=True)
    end_date = models.DateTimeField(blank=True)

class ShoppingItem(models.Model):
    quantity = models.IntegerField(blank=True)
    product = models.ForeignKey(Product,null=True, blank=True)
    basket = models.ForeignKey(Basket,null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True)
    state = models.CharField(max_length=10, blank=True)
    session = models.CharField(max_length=50, null=True, blank=True)
    create_date = models.DateTimeField(null=True,blank=True, default=timezone.now)

    def __str__(self):
        return 'El shoppItem se creo de manera correcta.'

    class Meta:
        verbose_name = 'ShoppingItem'
        verbose_name_plural = 'ShoppingItems'
        ordering = ('id',)




