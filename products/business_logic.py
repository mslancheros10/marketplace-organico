from main.models import Product

from django.utils import timezone

'''
    Transform product to json format
'''


def product_to_json(product):
    object = {
        'name': product.name,
        'price': product.price,
        'image_url': product.image_url,
        'unit_value': product.unit_value,
        'unit_name': product.unit_name
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


def get_certified_products():
    products=[]
    temp = Product.objects.all()\
        .only('name','price','image_url','unit_value','unit_name','farm__provider__certificado')\
        .filter(farm__provider__certificado=True)
    for p in temp:
        products.append(product_to_json(p))
    return products