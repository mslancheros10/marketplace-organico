from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from main.models import Product, ShoppingItem, User

import business_logic

import json

'''
    Add product to ShooppingItems
'''
@csrf_exempt
def addProduct(request, id):
    if request.method == 'GET':
        idProducto = id

        if request.user.is_authenticated():
            idUser = request.user.id
        else:
            idUser = -1

        'Se consulta si el producto ya se agrego al carrito para un usuario especifico en caso de que si entonces se aumenta en 1 la cantidad del mismo '
        try:
            shopItem = ShoppingItem.objects.get(product=idProducto, state='activo', user=idUser)
            total = shopItem.quantity
        except ShoppingItem.DoesNotExist:
            shopItemAux = None
            total = 0
        if total > 0:
            shopItem.quantity += 1
            shopItem.save()
            respuesta = 'Nueva cantidad del producto: ' + str(shopItem.quantity)
        else:
            product = Product.objects.get(id=idProducto)
            shopItem = ShoppingItem()
            shopItem.product = product
            shopItem.quantity = 1;
            shopItem.state = 'activo'
            if idUser > -1:
                user = User.objects.get(id=idUser)
                shopItem.user = user;

            shopItem.save()

            respuesta = 'se crea el nuevo item en shoppingItems'
        response = 'Fue ingresado. por el usuario: '+str(idUser) + 'total de productos al momento=' +str(total) + '- resultado final: '+ respuesta

        return JsonResponse(response, safe=False)
