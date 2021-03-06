from main.models import Provider
from main.models import Farm
from django.contrib.auth.models import User

from django.utils import timezone

'''
    Transform provider to json format
'''
def provider_to_json(farm):
    object = {
        'username': farm.provider.user.username,
        'firstName': farm.provider.user.first_name,
        'lastName': farm.provider.user.last_name,
        'email': farm.provider.user.email,
        'certificado': farm.provider.certificado,
        'farm': farm.name,
        'latitud': farm.latitude,
        'longitude': farm.longitude,
        'size': farm.size
    }
    return object




'''
    Method returning all providers
'''
def get_providers_from_model():
    farm = []
    for p in Farm.objects.all().filter(provider__active=True):
        farm.append(provider_to_json(p))

    return farm


def get_providers_certified():
    farm=[]
    temp = Farm.objects.all().filter(provider__active=True)\
        .only('name','latitude','longitude','size','provider__certificado')\
        .filter(provider__certificado=True)
    for p in temp:
        farm.append(provider_to_json(p))
    return farm
