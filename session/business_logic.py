from django.contrib.auth import authenticate, login
import json

from django.contrib.auth.models import User

from main.models import Provider, Farm

'''
    Perform login
'''


def login_request(request):
    json_user = json.loads(request.body.decode('utf-8'))

    print json_user

    username = json_user.get('username')
    password = json_user.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        message = 'El usuario ha iniciado sesion'
        status = 'OK'
    else:
        message = 'Usuario o Clave incorrecta'
        status = 'ERROR'

    print message

    print request.user.is_authenticated()

    return {
        'username': username,
        'status': status,
        'message': message
    }


def register_provider(request):

    json_provider = json.loads(request.body.decode('utf-8'))

    print json_provider

    username = json_provider.get('username')
    password = json_provider.get('password')
    is_certified = json_provider.get('certified')

    farm_name = json_provider.get('farm_name')
    farm_latitude = json_provider.get('farm_latitude')
    farm_longitude = json_provider.get('farm_longitude')
    farm_size = str(json_provider.get('farm_size'))+str(' hectareas')


    existUser = User.objects.filter(username=username)
    print existUser
    if existUser.count() > 0:
        return {'status': 'Usuario ya existe'}

    userModel = User.objects.create_user(username=username, password=password)
    userModel.save()
    print 'usuario creado'

    provider = Provider(user=userModel,certificado=is_certified)
    provider.save()

    farm = Farm(name=farm_name,latitude=farm_latitude,longitude=farm_longitude,size=farm_size,provider=provider)
    farm.save()

    return {'status': 'OK'}
