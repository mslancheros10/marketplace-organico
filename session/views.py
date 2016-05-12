from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.core.mail import send_mail, EmailMultiAlternatives

import business_logic
from django.contrib.auth import logout

from main.models import Provider

import json

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
    rol = 'client'
    if request.user.is_authenticated():
        logged = True

        existAsProvider = Provider.objects.filter(user__username=request.user.username)

        if existAsProvider.count() > 0:
            rol = 'provider'
    else:
        logged = False
    print logged
    return JsonResponse({'logged': logged, 'rol': rol})


'''
    Logout user
'''


@csrf_exempt
def logout_user(request):
    logout(request)
    return JsonResponse({'logout': True})


'''
    Register provider
'''


@csrf_exempt
def register_provider(request):
    if request.method == 'POST':
        response = business_logic.register_provider(request)
        print response
        return JsonResponse(response)

'''
    Register client
'''


@csrf_exempt
def register_client(request):
    if request.method == 'POST':
        response = business_logic.register_client(request)
        print response
        return JsonResponse(response)

'''
    PQR user
'''


@csrf_exempt
def comments(request):
    if request.method == 'POST':
        userEmail = request.user.email
        objs = json.loads(request.body)
        comment = objs['comment']

        comentario = "<strong>Comentario:</strong> %s <br><br><strong>Enviado por:</strong> %s" % (comment, userEmail)

        emailComentario = 'grupo5procesos2016@gmail.com'
        asunto = 'MpOrganico - Comentario'
        text_content = ''
        html_content = comentario
        from_email = userEmail
        to = emailComentario

        mensaje = EmailMultiAlternatives(asunto, text_content, from_email, [to])
        mensaje.attach_alternative(html_content, "text/html")
        mensaje.send()

    return JsonResponse({})
