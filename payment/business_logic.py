from main.models import ShoppingItem, Product, User, Payment
from baskets import business_logic as Bask
from products import business_logic as Prod
from shoppingItems import business_logic as shp

from django.core.exceptions import ObjectDoesNotExist

import json

import datetime


def pay_cart(user):
    temp = ShoppingItem.objects.all()\
        .filter(state='activo', user=user.id)
    price = update_number_of_items(temp)
    payment = Payment()
    payment.price = price
    payment.user = user
    payment.date = datetime.datetime.now()
    payment.save()
    return payment

def update_number_of_items(temp):
    price = 0
    for t in temp:
        if t.product is not None:
            if t.product.quantity-t.quantity >=0:
                t.product.quantity= t.product.quantity - t.quantity
            else:
                t.product.quantity=0
            price = price + (t.product.price*t.quantity)
            t.product.save()
        t.delete()
    return price

def pay_cart_rest(user):
    temp = ShoppingItem.objects.all()\
        .filter(state='activo', user=user.id)
    price = update_number_of_items_rest(temp)
    if price is not None:
        payment = Payment()
        payment.price = price
        payment.user = user
        payment.date = datetime.datetime.now()
        payment.save()
        return payment
    else:
        return None

def update_number_of_items_rest(temp):
    price = 0
    for t in temp:

        if t.product is not None:
            if t.product.quantity == 0:
                return None
            if t.product.quantity-t.quantity >=0:
                t.product.quantity= t.product.quantity - t.quantity
            else:
                t.product.quantity=0
            price = price + (t.product.price*t.quantity)
            t.product.save()
    return price

def purchsed_items(user):

    payment = Payment.objects.all().filter(user=user)
    if not payment:
        temp = []
    else:
        temp = shp.get_shoppingItems_from_model(user.id)
    return temp
