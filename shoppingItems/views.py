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

@csrf_exempt
def addProduct_rest(request):
    status = 'Error'
    message = 'No se pudo agregar el producto al carrito.'
    existItem = True
    existProduct= True
    product = None

    if request.method == 'PUT':
        objs = json.loads(unicode(request.body, "utf-8" ))
        username  = objs['username']
        id_product  = objs['id_product']
        quantity  = objs['quantity']

        if(username <> "" and id_product <> "" and quantity > 0):
            if request.user.is_authenticated():
                if username == request.user.username:
                    idUser = request.user.id
                    idProducto = int(id_product)

                    'Se consulta si el producto ya se agrego al carrito para un usuario especifico en caso de que si entonces se aumenta en X la cantidad del mismo '
                    try:
                        shopItem = ShoppingItem.objects.get(product=idProducto, state = 'activo', user=idUser)
                    except ShoppingItem.DoesNotExist:
                        existItem = False

                    try:
                        product = Product.objects.get(id=idProducto)
                    except ObjectDoesNotExist:
                        existProduct = False

                    if existItem:
                        shopItem.quantity += quantity
                        shopItem.save()
                        status = 'OK'
                    else:
                        if existProduct:
                            shopItem = ShoppingItem()
                            shopItem.quantity = quantity
                            shopItem.state = 'activo'
                            shopItem.product = product

                            if idUser > -1:
                                user = User.objects.get(id=idUser)
                                shopItem.user = user
                                shopItem.save()
                                status = 'OK'
                        else:
                            message = 'El producto no existe.'

                    if(status == 'OK'):
                        message = 'Agregado al Carrito.'
                else:
                    message = 'El username no coincide con el del usuario autenticado.'
            else:
                message = 'El usuario no se encuentra autenticado.'
        else:
            message = 'Los parametros de entradas estan incompletos.'
    else:
        message = 'Se requiere hacer la solicitud mediante el metodo PUT.'







    return JsonResponse({'status': status, 'message': message})

