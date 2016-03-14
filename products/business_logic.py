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
