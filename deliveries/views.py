from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import business_logic

'''
    REST Service retrieving current delivery
'''


@csrf_exempt
def get_dates(request):
    if request.method == 'GET':
        user = request.user
        response = business_logic.get_delivery_dates(user)

        return JsonResponse(response, safe=False)


