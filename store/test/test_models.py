from django.test import TestCase, testcases
from store.models import Category, product
from django.contrib.auth.models import User


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')

    def test_category_model_entry(self):

        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_entry(self):

        data = self.data1
        self.assertEqual(str(data), 'django')

    
class TestProductsModel(TestCase):
    def setUp(self):
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        self.data1 = product.objects.create(category_id=1, title ='django beginners', created_by_id=1,
        slug='django-beginners', price='20.00', images='django')

    def test_products_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, product))
        self.assertEqual(str(data), 'django beginners')








