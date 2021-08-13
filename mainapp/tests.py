from django.test import TestCase
from mainapp.models import ProductCategory, Product
from django.test.client import Client

# Create your tests here.


class TestMainSmokeTest(TestCase):
    status_code_success = 200

    def setUp(self):
        category_1 = ProductCategory.objects.create(
            name=f'category 1'
        )
        for i in range(100):
            Product.objects.create(
                category=category_1,
                name=f'product {i}'
            )
        self.client = Client()

    def test_mainapp_urls(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, self.status_code_success)

    def test_product_url(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, self.status_code_success)

