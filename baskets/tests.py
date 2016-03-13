from django.test import TestCase

from main.models import Basket, Product, ShoppingItem

import business_logic

# Create your tests here.
END_DATE = '2016-03-30T15:19:21+00:00'
START_DATE = '2016-03-01T15:19:21+00:00'
PAPAYA = 'Papaya'
CANASTA_DE_TEST = 'Canasta de Test'


class BasketsCase(TestCase):
    def setUp(self):
        product = Product.objects.create(name=PAPAYA, price=3000)
        basket = Basket.objects.create(name=CANASTA_DE_TEST, start_date=START_DATE, end_date=END_DATE)
        ShoppingItem.objects.create(quantity=2,product=product,basket=basket)

    def test_get_baskets(self):
        baskets = business_logic.get_baskets_from_model()
        print baskets

        self.assertIsNotNone(baskets)

        first_basket = baskets[0]
        print first_basket

        self.assertIsNotNone(first_basket)

        self.assertEqual(first_basket.get('name'), CANASTA_DE_TEST, 'Nombre de Canasta mal')

        self.assertIsNotNone(first_basket.get('products'))

        product = first_basket.get('products')[0]

        print product

        self.assertEqual(product.get('name'),PAPAYA,'Nombre del producto mal')




