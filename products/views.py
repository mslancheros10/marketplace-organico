from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

import business_logic
from django.conf import settings

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

@csrf_exempt
def add_product_list(request):
    if request.user.is_superuser:
        return HttpResponseRedirect('/#/addProducts/')
    else:
        return HttpResponseRedirect('/admin/')

@csrf_exempt
def register_product_list(request):
    if request.user.is_superuser:
        objs = json.loads(request.body)
        business_logic.register_products(objs['list'])
        return HttpResponse('OK')
    else:
        return HttpResponse('FAILADMIN')



