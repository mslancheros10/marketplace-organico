from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Farm(models.Model):
    name = models.CharField(max_length=100,blank=True)
    latitude = models.CharField(max_length=100,blank=True)
    longitude = models.CharField(max_length=100,blank=True)
    size = models.CharField(max_length=100,blank=True) # 5 hectareas
    type = models.CharField(max_length=100,blank=True) #certified / no_certified
    provider = models.OneToOneField(User,null=True)

class Product(models.Model):
    name = models.CharField(max_length=100,blank=True)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    image_url = models.CharField(max_length=1000,blank=True)
    unit_value = models.CharField(max_length=100,blank=True)
    unit_name = models.CharField(max_length=100,blank=True)
    farm = models.ForeignKey(Farm,null=True)

class Basket(models.Model):
    name = models.CharField(max_length=100,blank=True)
    start_date = models.DateTimeField(blank=True)
    end_date = models.DateTimeField(blank=True)

class ShoppingItem(models.Model):
    quantity = models.IntegerField(blank=True)
    product = models.ForeignKey(Product,null=True)
    basket = models.ForeignKey(Basket,null=True)


