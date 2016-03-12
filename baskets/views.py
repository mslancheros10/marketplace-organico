from django.http import HttpResponse
from django.core import serializers

import business_logic

# Constants
JSON = "json"

'''
    REST Service retrieving current baskets
'''
def getBaskets(request):
    if request.method == 'GET':
        baskets = business_logic.getBasketsFromModel()
        return HttpResponse(serializers.serialize(JSON, baskets))


