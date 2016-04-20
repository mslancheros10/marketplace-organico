from main.models import Delivery
from django.contrib.auth.models import User

from datetime import date, timedelta
import time

'''
    Transform delivery to json format
'''
def delivery_to_json(delivery):
    object = {
        'date': delivery.date,
        'day': delivery.day,
        'address': delivery.address,
        'phone': delivery.phone
    }
    return object




'''
    Method returning dates of delivery
'''
def get_delivery_dates(user):
    dates = []
    diaActual = time.strftime("%w")

    if diaActual == '1' or diaActual == '2' or diaActual == '6' or diaActual == '7':
        dia1 = 'MIERCOLES'
        dia2 = 'SABADO'
    else:
        dia1 = 'SABADO'
        dia2 = 'MIERCOLES'

    fecha1 = get_dates_by_day(date.today())
    fecha2 = get_dates_by_day(fecha1)

    delivery = Delivery()
    delivery.date = fecha1
    delivery.day = dia1
    delivery.address = ''
    delivery.phone = ''

    dates.append(delivery_to_json(delivery))

    deliveryT = Delivery()
    deliveryT.date = fecha2
    deliveryT.day = dia2
    deliveryT.address = ''
    deliveryT.phone = ''

    dates.append(delivery_to_json(deliveryT))

    return dates


def get_dates_by_day(fecha):
    d=fecha+timedelta(days=1)

    if fecha.strftime("%w") == '1':
        d=fecha+timedelta(days=2)
    elif fecha.strftime("%w") == '2':
        d=fecha+timedelta(days=1)
    elif fecha.strftime("%w") == '3':
        d=fecha+timedelta(days=3)
    elif fecha.strftime("%w") == '4':
        d=fecha+timedelta(days=2)
    elif fecha.strftime("%w") == '5':
        d=fecha+timedelta(days=1)
    elif fecha.strftime("%w") == '6':
        d=fecha+timedelta(days=4)
    elif fecha.strftime("%w") == '7':
        d=fecha+timedelta(days=3)

    return d

