from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from main.models import Product, Basket, ShoppingItem, User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.sessions.models import Session

import business_logic

import json

'''
    Add product to ShooppingItems
'''
@csrf_exempt
def addProduct(request, id, tipo):
    if request.method == 'GET':
        response = ''
        existItem = True
        existProduct= True
        existBasket = True
        basket = None
        product = None
        total = 0

        idProducto = id
        tipoProducto = tipo


        if request.user.is_authenticated():
            idUser = request.user.id

            'Se consulta si el producto ya se agrego al carrito para un usuario especifico en caso de que si entonces se aumenta en 1 la cantidad del mismo '


            if tipoProducto == 'canasta':
                try:
                    shopItem = ShoppingItem.objects.get(basket=idProducto, state='activo', user=idUser)
                    total = shopItem.quantity
                except ObjectDoesNotExist:
                    existItem = False

                try:
                    basket = Basket.objects.get(id=idProducto)
                except ObjectDoesNotExist:
                    existBasket = False
            else:
                try:
                    shopItem = ShoppingItem.objects.get(product=idProducto, state='activo', user=idUser)
                    total = shopItem.quantity
                except ShoppingItem.DoesNotExist:
                    existItem = False

                try:
                    product = Product.objects.get(id=idProducto)
                except ObjectDoesNotExist:
                    existProduct = False

            if existItem:
                shopItem.quantity += 1
                shopItem.save()
                respuesta = 'Nueva cantidad del producto: ' + str(shopItem.quantity)
            else:
                shopItem = ShoppingItem()
                shopItem.quantity = 1;
                shopItem.state = 'activo'

                if existProduct: shopItem.product = product

                if existBasket: shopItem.basket = basket

                if idUser > -1:
                    user = User.objects.get(id=idUser)
                    shopItem.user = user;

                shopItem.save()
                respuesta = 'se crea el nuevo item en shoppingItems'

            response = 'El producto ('+ idProducto +') de tipo ('+ tipoProducto +') fur agregado y relacionado al usuario ('+str(idUser) + ') Total de productos antes del proceso (' +str(total) + ') - Resultado final: '+ respuesta
        else:
            response = 'no autenticado'

        '''
        response = 'Producto: '+ idProducto + '- tipo: '+ tipoProducto + ' - session:'+ sesion
        '''

        return JsonResponse(response, safe=False)

'''
    REST Service retrieving current shoppinItems
'''
@csrf_exempt
def get_shoppinItems(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            idUser = request.user.id
        else:
            idUser = -1

        response = business_logic.get_shoppinItems_from_model(idUser)

        return JsonResponse(response,safe=False)
