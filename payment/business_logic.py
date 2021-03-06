from main.models import ShoppingItem, Product, User, Payment
from baskets import business_logic as Bask
from products import business_logic as Prod

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
        '''
        for b in t.baskets:
            if b.quantity-t.quantity >=0:
                b.quantity= b.quantity - t.quantity
                price = price + (b.price*t.quantity)
            else:
                b.quantity=0
            price = price + (b.price*t.quantity)
            b.save()
            '''
        if t.product is not None:
            if t.product.quantity-t.quantity >=0:
                t.product.quantity= t.product.quantity - t.quantity
            else:
                t.product.quantity=0
            price = price + (t.product.price*t.quantity)
            t.product.save()
        t.delete()
    return price


