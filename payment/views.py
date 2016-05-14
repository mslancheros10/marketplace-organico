from django.contrib.auth import authenticate
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


@csrf_exempt
def pay_cart_rest(request):
    response = ''
    if request.method == 'POST':
        objs = json.loads(request.body.decode('utf-8'))
        print objs
        username = objs['username']
        password = objs['password']
        confirmation = objs['confirmation']
        if confirmation:
            user = authenticate(username=username, password=password)
            if user is None:
                return JsonResponse({'status':'ERROR','message':'El usuario no exite'})
            pago = business_logic.pay_cart_rest(user)
            if pago is None:
                return JsonResponse({'status':'OK','message':'Confirmada la compra.'})
            else:
                return JsonResponse({'status':'ERROR','message':'Producto Agotado.'})
        else:
            return JsonResponse({'status':'ERROR','message':'Confirmacion en False.'})

@csrf_exempt
def view_order_rest(request):
    if request.method == 'GET':
        user = request.user
        if user.is_anonymous():
            print 'No hay Usuario Creado'
            return JsonResponse({})
        else:
            list=business_logic.purchsed_items(user)
            return JsonResponse(list)
