from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory
from main.models import Basket, Product, ShoppingItem
from shoppingItems.views import addProduct

# Create your tests here.

END_DATE = '2017-03-30T15:19:21+00:00'
START_DATE = '2015-03-01T15:19:21+00:00'
PAPAYA = 'Papaya'
CANASTA_DE_TEST = 'Canasta de Test'
USERNAME_TEST = 'jacob'

class ShoppingItemsCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username=USERNAME_TEST, email='', password='top_secret')

        product = Product.objects.create(name=PAPAYA, price=3000)
        basket = Basket.objects.create(name=CANASTA_DE_TEST, start_date=START_DATE, end_date=END_DATE)
        self.shoppingItem = ShoppingItem.objects.create(quantity=2, user=self.user, product=product, state='activo')
        self.shoppingItem2 = ShoppingItem.objects.create(quantity=1, user=self.user, basket=basket, state='activo')


    def test_add_product(self):
        # Create an instance of a GET request.
        request = self.factory.get('/customer/details')

        # Recall that middleware are not supported. You can simulate a
        # logged-in user by setting request.user manually.
        request.user = self.user

        # Test my_view() as if it were deployed at /customer/details
        response = addProduct(request, self.shoppingItem.product.id, 'product')

        #response.status_code = 300

        self.assertEqual(response.status_code, 200, 'El metodo addProduct de shoppingItem respondio un status_code diferente a 200')
        self.assertIsNotNone(self.shoppingItem.product)

        first_product = self.shoppingItem.product
        print first_product
        self.assertIsNotNone(first_product)
        self.assertEqual(first_product.name, PAPAYA, 'El nombre del producto asociado al shoppItem esta mal')
        self.assertEqual(first_product.price, 3000, 'El precio del producto asociado al shoppItem esta mal')

        first_basket = self.shoppingItem2.basket
        print first_basket
        self.assertIsNotNone(first_basket)
        self.assertEqual(first_basket.name, CANASTA_DE_TEST, 'El nombre de la canasta asociada al shoppItem esta mal')

        first_shoppItem = self.shoppingItem
        print first_shoppItem
        self.assertIsNotNone(first_shoppItem)
        self.assertEqual(first_shoppItem.quantity, 2, 'La cantidad asociada al shoppItem esta mal')
        self.assertEqual(first_shoppItem.user.username, USERNAME_TEST, 'El username del usuario asociado al shoppItem esta mal')
        self.assertEqual(first_shoppItem.state, 'activo', 'El estado asociado al shoppItem esta mal')




