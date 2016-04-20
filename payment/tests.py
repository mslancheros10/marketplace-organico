from django.test import TestCase
from django.contrib.auth.models import User
from main.models import Payment

import datetime

class PaymentCase(TestCase):
    # Create your tests here.
    def test_add_payment(self):

        payment = Payment.objects.create(price=50000,
                                         date=datetime.datetime.now(),
                                         user=User.objects.create_user(
                                             username='username_test',
                                             email='',
                                             password='top_secret'))
        payment.save()
        payment2 = Payment.objects.get(price=50000)

        self.assertEqual(50000, payment2.price, 'El producto esta mal')
