from main.models import Product, Farm
import json
from math import fabs

from django.utils import timezone

'''
    Transform product to json format
'''


def product_to_json(product):
    object = {
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'unit': product.unit_name,
        'image': product.image_url,
        'stock': product.quantity,
        'unit_value': product.unit_value,
        'description': product.description,
        'nameFarm': product.farm.name
    }
    return object

'''
    Transform product to json format
'''


def product_to_json_rest(product):
    object = {
        'id': str(product.id),
        'name': product.name,
        'price': float(product.price),
        'unit': product.unit_name,
        'premium': product.premium,
        'image': product.image_url,
        'stock': product.quantity
    }
    return object

'''
    Method returning all products
'''


def get_products_from_model():

    products = []

    for p in Product.objects.all():
        products.append(product_to_json(p))

    return products

'''
    Method returning all products
'''


def get_products_from_model_rest():

    products = []

    for p in Product.objects.all():
        products.append(product_to_json_rest(p))

    return products

'''
    Method returning product details
'''


def get_product_details(id):

    product = Product.objects.get(id=id)
    product = product_to_json(product)
    return product

def get_certified_products():
    products=[]
    temp = Product.objects.all()\
        .only('name','price','image_url','unit_value','unit_name','farm__provider__certificado')\
        .filter(farm__provider__certificado=True)
    for p in temp:
        products.append(product_to_json(p))
    return products


'''
    Method returning product of farm
'''

def get_products_farm(user):
    products = []
    temp = Product.objects.all()\
        .only('name','price','image_url','unit_value','unit_name','farm__provider__user')\
        .filter(farm__provider__user=user)
    for p in temp:
        products.append(product_to_json(p))

    return products

def register_products(objs):
    products = json.loads(objs)
    print products
    for p in products:
        print p
        product = Product()
        product.name = p['name']
        product.price = p['price']
        product.image_url = p['image_url']
        product.unit_value = p['unit_value']
        product.unit_name = p['unit_name']
        farm = Farm.objects.get(id=p['farm'])
        product.farm = farm
        product.description = p['description']
        product.quantity = p['quantity']
        product.save()
        print 'objeto guardado'


'''
    Method add product of farm
'''
def addProduct(user, id, unit_name, unit_value, price, quantity):

    print 'Entro BL addProduct'

    product = Product();

    productActual = Product.objects.get(id=id)

    farm = Farm.objects.all().filter(provider__active=True)\
        .only('name','latitude','longitude','size','provider__certificado')\
        .filter(provider__user=user)

    print 'Image: ' + productActual.image_url

    product.image_url = productActual.image_url
    product.description = productActual.description
    product.name = productActual.name
    product.price = price
    product.unit_value = unit_value
    product.unit_name = unit_name
    product.farm = farm[0]
    product.quantity = quantity

    product.save()

    listProduct = get_products_farm(user);

    return listProduct

def register_products(objs):
    products = json.loads(objs)
    print products
    for p in products:
        print p
        product = Product()
        product.name = p['name']
        product.price = p['price']
        product.image_url = p['image_url']
        product.unit_value = p['unit_value']
        product.unit_name = p['unit_name']
        farm = Farm.objects.get(id=p['farm'])
        product.farm = farm
        product.description = p['description']
        product.quantity = p['quantity']
        product.save()
        print 'objeto guardado'