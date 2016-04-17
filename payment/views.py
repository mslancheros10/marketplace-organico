from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from main.models import Product, Basket, ShoppingItem, User
from django.core.exceptions import ObjectDoesNotExist

import business_logic

import json


@csrf_exempt
def pay_cart(request):
    if request.method == 'POST':
        if request.user.is_authenticated():
            user = request.user
        else:
            user = None

        objs = json.loads(request.body)

        response = business_logic.pay_cart(user)
        return JsonResponse("OK",safe=False)
