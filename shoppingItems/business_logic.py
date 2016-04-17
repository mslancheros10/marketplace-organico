from main.models import ShoppingItem, Product, User
from baskets import business_logic as Bask
from products import business_logic as Prod

from django.core.exceptions import ObjectDoesNotExist

import json


'''
    Method returning all shoppingItems
'''

def get_shoppinItems_from_model(idUser):

    shoppingItems = []

    temp = ShoppingItem.objects.all()\
        .filter(state='activo', user=idUser)

    for b in temp:
        shoppingItems.append(shoppingItems_to_json(b))

    return shoppingItems

'''
    Transform shoppingItems to json format
'''
def shoppingItems_to_json(shoppingItem):

    object = {
        'quantity':shoppingItem.quantity,
        'state': shoppingItem.state,
        'baskets': Bask.get_basket_products(shoppingItem.basket),
        'products': get_shoppingItem_products(shoppingItem.product)
    }

    return object

def get_shoppingItem_products(product):
    products = []
    try:
        products.append(Prod.product_to_json(product))
    except:
        print 'Error..'

    return products
