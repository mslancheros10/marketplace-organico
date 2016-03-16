from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import business_logic

'''
    REST Service retrieving current baskets
'''


@csrf_exempt
def get_baskets(request):
    if request.method == 'GET':
        response = business_logic.get_baskets_from_model()
        print response
        return JsonResponse(response,safe=False)


