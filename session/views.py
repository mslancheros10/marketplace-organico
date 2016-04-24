from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import business_logic
from django.contrib.auth import logout
'''
    REST Service performing login
'''


@csrf_exempt
def login_request(request):
    if request.method == 'POST':
        response = business_logic.login_request(request)
        print response
        return JsonResponse(response)


'''
    Check if user is logged
'''

@csrf_exempt
def is_logged_user(request):
    if request.user.is_authenticated():
        logged = True
    else:
        logged = False
    print logged
    return JsonResponse({'logged':logged})

'''
    Logout user
'''

@csrf_exempt
def logout_user(request):
    logout(request)
    return JsonResponse({'logout':True})


'''
    Register provider
'''

@csrf_exempt
def register_provider(request):
    if request.method == 'POST':
        response = business_logic.register_provider(request)
        print response
        return JsonResponse(response)