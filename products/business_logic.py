from math import fabs

from main.models import Product, Farm

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


'''
    Method add product of farm
'''
def addProduct(user):

    print 'Entro BL addProduct'

    product = Product()
    farm = Farm.objects.all().filter(provider__active=True)\
        .only('name','latitude','longitude','size','provider__certificado')\
        .filter(provider__user=user)

    product.name = 'Apio'
    product.price = '1000'
    product.image_url = ''
    product.unit_value = '10'
    product.unit_name = 'libras'
    product.farm = farm[0]
    product.description = 'Apio'
    product.quantity = '50'

    product.save()

    return product