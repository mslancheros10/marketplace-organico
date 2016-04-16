from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import business_logic

'''
    REST Service retrieving current providers
'''


@csrf_exempt
def get_providers(request):
    if request.method == 'GET':
        response = business_logic.get_providers_from_model()
        print response
        return JsonResponse(response, safe=False)

def get_providers_certified(request):
    if request.method == 'GET':
        response = business_logic.get_providers_certified()
        print response
        return JsonResponse(response, safe=False)

