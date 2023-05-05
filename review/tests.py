from django.test import TestCase
from product.models import Product
# class ProductTestCase(TestCase):
#     def setUp(self):
#         Product.objects.create(name="Test Product", price=10.99)

#     def test_product_name(self):
#         product = Product.objects.get(name="Test Product")
#         self.assertEqual(product.name, "Test Product")
    
#     def test_product_price(self):
#         product = Product.objects.get(name="Test Product")
#         self.assertAlmostEqual(product.price, 10.99, places=2)

class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="Test", price=42)

    def test_model_fields(self):
        obj = Product.objects.get(name="Test")
        self.assertEqual(obj.name, "Test")
        self.assertEqual(obj.price, 42)