from main.models import Basket, ShoppingItem

from django.utils import timezone

'''
    Convert product to json
'''


def shopping_item_to_json(shopping_item):
    object = {
        'quantity': shopping_item.quantity,
        'name': shopping_item.product.name,
        'price': shopping_item.product.price,
        'image_url': shopping_item.product.image_url,
        'unit_value': shopping_item.product.unit_value,
        'unit_name': shopping_item.product.unit_name,
    }
    return object


'''
    Get products from specific basket
'''


def get_basket_products(basket):
    products = []

    for p in ShoppingItem.objects.filter(basket=basket, state='promocion'):
        products.append(shopping_item_to_json(p))

    return products


'''
    Transform basket to json format
'''


def basket_to_json(basket):
    object = {
        'id':basket.pk,
        'name': basket.name,
        'start_date': basket.start_date,
        'end_date': basket.end_date,
        'products': get_basket_products(basket)
    }
    return object


'''
    Method returning all baskets
'''


def get_baskets_from_model():

    baskets = []

    for b in Basket.objects.filter(start_date__lte=timezone.now(),end_date__gte=timezone.now()):
        baskets.append(basket_to_json(b))

    return baskets

'''
    Metodo que devuelve el valor total de una canasta.
'''


def get_basket_price(basket):
    price = 0

    baskets = ShoppingItem.objects.filter(basket=basket, state='promocion').only('product__price')

    for b in baskets:
        price += b.quantity * b.product.price

    return price
