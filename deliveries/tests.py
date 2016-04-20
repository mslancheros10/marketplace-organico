from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory
from main.models import Delivery
from deliveries.views import get_dates

# Create your tests here.

USERNAME_TEST = 'pruebas'

class DeliveriesCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username=USERNAME_TEST, email='', password='top_secret')

        delivery = get_dates()





