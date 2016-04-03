from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import business_logic

'''
    REST Service performing login
'''


@csrf_exempt
def login_request(request):
    if request.method == 'POST':
        response = business_logic.login_request(request)
        print response
        return JsonResponse({'message':response})


