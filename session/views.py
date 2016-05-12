from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.core.mail import send_mail, EmailMultiAlternatives

import business_logic
from django.contrib.auth import logout

from main.models import Provider, Client

import json

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

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
    Get info client
'''


@csrf_exempt
def get_client(request):
    status = 'Error'
    username = ''
    email = ''
    address = ''
    phone = ''

    if request.method == 'POST':
        '''
        response = business_logic.getClient(request)
        '''
        if request.user.is_authenticated():
            username = request.user.username
            firstname = request.user.first_name
            lastname = request.user.last_name
            email = request.user.email

            try:
                client = Client.objects.get(user__username=username)
                address = client.address
                phone = client.phone
            except ObjectDoesNotExist:
                print 'No existe info adicional de cliente.'

            status = 'OK'
        else:
            status = 'Usuario no autenticado'
    else:
        status = 'Metodo no POST'

    return JsonResponse({'status':status,
                        'username':username,
                         'firstname':firstname,
                         'lastname':lastname,
                        'email':email,
                         'address':address,
                         'phone':phone
                        })

'''
    Update info client
'''

@csrf_exempt
def update_client(request):
    status = 'Error'
    address = ''
    phone = ''

    if request.method == 'POST':
        json_client = json.loads(request.body.decode('utf-8'))

        print json_client

        username = json_client.get('username')
        firstname = json_client.get('firstname')
        lastname = json_client.get('lastname')
        email = json_client.get('email')
        address = json_client.get('address')
        phone = json_client.get('phone')

        try:
            userModel = User.objects.get(username=username)
            userModel.first_name = firstname
            userModel.last_name = lastname
            userModel.email = email
            userModel.save()

            try:
                client = Client.objects.get(user__username=username)
                client.address = address
                client.phone = phone
                client.active = 1
                client.save()
            except ObjectDoesNotExist:
                if(address <> "" or phone <> ""):
                    client = Client()
                    client.user = userModel
                    client.address = address
                    client.phone = phone
                    client.active = 1
                    client.save()
                else:
                    print 'No existe info adicional de cliente.'

            status = 'OK'
        except ObjectDoesNotExist:
            status = 'Usuario no existe.'

    else:
        status = 'Metodo no POST.'

    return JsonResponse({'status': status})

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
