from main.models import Product, Farm
import json

from django.utils import timezone

'''
    Transform product to json format
'''


def product_to_json(product):
    object = {
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'image_url': product.image_url,
        'unit_value': product.unit_value,
        'unit_name': product.unit_name,
        'description': product.description,
        'quantity': product.quantity,
        'nameFarm': product.farm.name
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