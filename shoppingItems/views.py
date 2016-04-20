from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from main.models import Product, Basket, ShoppingItem, User
from django.core.exceptions import ObjectDoesNotExist

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

        idProducto = id
        tipoProducto = tipo


        if request.user.is_authenticated():
            idUser = request.user.id

            'Se consulta si el producto ya se agrego al carrito para un usuario especifico en caso de que si entonces se aumenta en 1 la cantidad del mismo '


            if tipoProducto == 'canasta':
                try:
                    shopItem = ShoppingItem.objects.get(basket=idProducto, state='activo', user=idUser)
                except ObjectDoesNotExist:
                    existItem = False

                try:
                    basket = Basket.objects.get(id=idProducto)
                except ObjectDoesNotExist:
                    existBasket = False
            else:
                try:
                    shopItem = ShoppingItem.objects.get(product=idProducto, state='activo', user=idUser)
                except ShoppingItem.DoesNotExist:
                    existItem = False

                try:
                    product = Product.objects.get(id=idProducto)
                except ObjectDoesNotExist:
                    existProduct = False

            if existItem:
                shopItem.quantity += 1
                shopItem.save()
            else:
                shopItem = ShoppingItem()
                shopItem.quantity = 1
                shopItem.state = 'activo'

                if existProduct: shopItem.product = product

                if existBasket: shopItem.basket = basket

                if idUser > -1:
                    user = User.objects.get(id=idUser)
                    shopItem.user = user

                shopItem.save()

            response = 'El producto se ingreso correctamente'
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
def get_shoppingItems(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            idUser = request.user.id
            response = business_logic.get_shoppingItems_from_model(idUser)
        else:
            response = 'no autenticado'

        return JsonResponse(response,safe=False)

'''
    Delete product of ShooppingItems
'''
@csrf_exempt
def deleteProduct(request, id):
    if request.method == 'GET':
        response = ''
        existItem = True


        if request.user.is_authenticated():
            idUser = request.user.id

            try:
                shopItem = ShoppingItem.objects.get(id=id, state='activo', user=idUser)
            except ObjectDoesNotExist:
                existItem = False

            if existItem:
                shopItem.delete()
                response = 'El producto se elimino correctamente'
            else:
                response = 'El shoppItem no existe.'
        else:
             response = 'no autenticado'

        return JsonResponse(response,safe=False)

