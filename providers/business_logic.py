from main.models import Provider
from django.contrib.auth.models import User

from django.utils import timezone

'''
    Transform provider to json format
'''
def provider_to_json(provider):
    object = {
        'username': provider.user.username,
        'firstName': provider.user.first_name,
        'lastName': provider.user.last_name,
        'email': provider.user.email,
        'certificado': provider.certificado
    }
    return object




'''
    Method returning all providers
'''
def get_providers_from_model():

    providers = []

    for p in Provider.objects.all():
        providers.append(provider_to_json(p))

    return providers
