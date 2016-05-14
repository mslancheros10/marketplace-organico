from django.contrib.auth import authenticate, login
import json

'''
    Perform login
'''
def login_request(request):

    json_user = json.loads(request.body.decode('utf-8'))

    print json_user

    username = json_user.get('username')
    password = json_user.get('password')

    user = authenticate(username=username,password=password)

    if user is not None:
        login(request,user)
        message = 'El usuario ha iniciado sesion'
        status = 'OK'
    else:
        message = 'Usuario o Clave incorrecta'
        status = 'ERROR'

    print message

    print request.user.is_authenticated()

    return {
        'username':username,
        'status':status,
        'message':message
    }