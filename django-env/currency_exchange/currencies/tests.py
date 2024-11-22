from django.test import TestCase
from django.urls import include, path
from rest_framework.test import APITestCase, URLPatternsTestCase
from rest_framework import status
from currencies.models import *


class CurrrencyAPITests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('', include('currencies.urls')),
    ]

    def test_can_get_currrency_list(self):
        test_curr = Currency(code='TES', reverse_rate=True)
        test_curr.save()
        url = ('/currency/')
        response = self.client.get(url, format='json')
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data, [{'code':'TES'}])

    def test_cant_delete_currency(self):
        url = ('/currency/')
        response = self.client.delete(url, format='json')
        self.assertTrue(status.is_client_error(response.status_code))

    def test_can_get_exchange_rate(self):
        test_rate = ExchangeRate(currency_pair='ABCXYZ', exchange_rate=1.123)
        test_rate.save()
        url=('/currency/ABC/XYZ/')
        response = self.client.get(url, format='json')
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data, [{'currency_pair':'ABCXYZ', 'exchange_rate':1.123}])

    def test_can_get_reversed_exchange_rate(self):
        test_rate = ExchangeRate(currency_pair='ABCXYZ', exchange_rate=1.123)
        test_rate.save()
        url=('/currency/XYZ/ABC/')
        response = self.client.get(url, format='json')
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data, [{'currency_pair':'ABCXYZ', 'exchange_rate':1.123}])


    def test_cant_delete_exchange_rate(self):
        url = ('/currency/ABC/XYZ/')
        response = self.client.delete(url, format='json')
        self.assertTrue(status.is_client_error(response.status_code))