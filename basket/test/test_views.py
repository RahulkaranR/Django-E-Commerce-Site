from msilib.schema import Class
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from store.models import Category, product


class TestBasketView(TestCase):
    def setUp(self):
        User.objects.create(username='admin')
        Category.objects.create(name='django', slug='django')
        product.objects.create(category_id=1, title ='django beginners', created_by_id=1,
        slug='django-beginners', price='20.00', images='django')
        product.objects.create(category_id=1, title ='django intermediate', created_by_id=1,
        slug='django-intermediate', price='20.00', images='django')
        product.objects.create(category_id=1, title ='django advanced', created_by_id=1,
        slug='django-advance', price='20.00', images='django')
        self.client.post(
            reverse('basket:basket_add'), {"productid": 1, "productqty":1, 'action':"post"}, xhr=True
        )
        self.client.post(
            reverse('basket:basket_add'), {"productid": 2, "productqty":2, 'action':"post"}, xhr=True
        )

    def test_basket_url(self):
        response = self.client.get(reverse('basket:basket_summery'))
        self.assertEqual(response.status_code, 200)

    def test_basket_add(self):
        response = self.client.post(
            reverse('basket:basket_add'), {"productid": 3, "productqty": 1, "action": 'post'}, xhr=True
        )
        self.assertEqual(response.json(), {'qty': 4})  


