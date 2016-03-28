from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

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

