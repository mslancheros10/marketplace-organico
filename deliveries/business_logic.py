from main.models import Delivery
from django.contrib.auth.models import User

import datetime
import calendar

'''
    Transform delivery to json format
'''
def delivery_to_json(delivery):
    object = {
        'date': delivery.date,
        'address': delivery.address,
        'phone': delivery.phone
    }
    return object




'''
    Method returning dates of delivery
'''
def get_delivery_dates(user):
    dates = []

    today=datetime.datetime.now()
    dateMonthStart="%s-%s-01" % (today.year, today.month)
    dateMonthEnd="%s-%s-%s" % (today.year, today.month, calendar.monthrange(today.year-1, today.month-1)[1])

    delivery = Delivery()
    delivery.date = dateMonthStart
    delivery.address = ''
    delivery.phone = ''

    dates.append(delivery_to_json(delivery))

    deliveryT = Delivery()
    deliveryT.date = dateMonthEnd
    deliveryT.address = ''
    deliveryT.phone = ''

    dates.append(delivery_to_json(deliveryT))

    return dates

