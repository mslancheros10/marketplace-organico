from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from main.models import Product, User
from django.core.exceptions import ObjectDoesNotExist

import json

import business_logic

'''
    REST Service retrieving current baskets
'''


@csrf_exempt
def get_products(request):
    if request.method == 'GET':
        response = business_logic.get_products_from_model()
        return JsonResponse(response,safe=False)

@csrf_exempt
def get_certified_products(request):
    if request.method == 'GET':
        response = business_logic.get_certified_products()
        return JsonResponse(response,safe=False)

'''
    REST Service retrieving a product detail
'''

@csrf_exempt
def details(request, id):
    if request.method == 'GET':
        response = business_logic.get_product_details(id)
        return JsonResponse(response, safe=False)

'''
    REST Service retrieving a product farm
'''

@csrf_exempt
def get_products_farm(request, name):
    if request.method == 'GET':
        response = business_logic.get_products_farm(name)
        return JsonResponse(response,safe=False)



'''
    Add product to Farm
'''
@csrf_exempt
def addProductFarm(request, name, quantity):

    if request.method == 'GET':
        idUser = request.user.id
        existItem = True

        try:
            products = Product.objects.get(name=name, user=idUser)
        except ObjectDoesNotExist:
            existItem = False

        if(products.quantity > 0):
            response = 'El producto ya existe en la lista de productos'
        else:
            products.save()
            response = 'El producto se ingreso correctamente'


        return JsonResponse(response, safe=False)
