from django.test import TestCase
from django.test import TestCase, RequestFactory
from main.models import Delivery
from deliveries.views import get_dates

from datetime import date, timedelta
import time


class DeliveryCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_get_dates(self):
        request = self.factory.get('/customer/deliveries')
        request.method = 'GET'

        fechaComparar = date.today()+timedelta(days=3)


        print fechaComparar

        self.assertEqual('2016-04-23', str(fechaComparar), 'Las fechas no son correctas')
