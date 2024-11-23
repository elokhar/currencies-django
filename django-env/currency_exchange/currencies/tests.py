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

    def test_can_get_exchange_rate_to_USD(self):
        test_rate = ExchangeRate(currency_pair='ABCUSD', exchange_rate=1.123)
        test_rate.save()
        url=('/currency/ABC/USD/')
        response = self.client.get(url, format='json')
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data, [{'currency_pair':'ABCUSD', 'exchange_rate':1.123}])

    def test_can_get_exchange_rate_from_USD(self):
        test_rate = ExchangeRate(currency_pair='USDABC', exchange_rate=1.123)
        test_rate.save()
        url=('/currency/USD/ABC/')
        response = self.client.get(url, format='json')
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data, [{'currency_pair':'USDABC', 'exchange_rate':1.123}])

    def test_can_get_reversed_exchange_rate_to_USD(self):
        test_rate = ExchangeRate(currency_pair='USDABC', exchange_rate=2)
        test_rate.save()
        url=('/currency/ABC/USD/')
        response = self.client.get(url, format='json')
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data, [{'currency_pair':'ABCUSD', 'exchange_rate':1/2}])

    def test_can_get_reversed_exchange_rate_from_USD(self):
        test_rate = ExchangeRate(currency_pair='ABCUSD', exchange_rate=2)
        test_rate.save()
        url=('/currency/USD/ABC/')
        response = self.client.get(url, format='json')
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data, [{'currency_pair':'USDABC', 'exchange_rate':1/2}])

    def test_can_get_exchange_rate_not_to_USD(self):
        test_rate1 = ExchangeRate(currency_pair='ABCUSD', exchange_rate=2)
        test_rate1.save()
        test_rate2 = ExchangeRate(currency_pair='DEFUSD', exchange_rate=8)
        test_rate2.save()
        url=('/currency/ABC/DEF/')
        response = self.client.get(url, format='json')
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data, [{'currency_pair':'ABCDEF', 'exchange_rate':1/4}])

    def test_can_get_exchange_rate_not_to_USD_one_reversed(self):
        test_rate1 = ExchangeRate(currency_pair='USDABC', exchange_rate=1/2)
        test_rate1.save()
        test_rate2 = ExchangeRate(currency_pair='DEFUSD', exchange_rate=8)
        test_rate2.save()
        url=('/currency/ABC/DEF/')
        response = self.client.get(url, format='json')
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data, [{'currency_pair':'ABCDEF', 'exchange_rate':1/4}])

    def test_can_get_exchange_rate_not_to_USD_both_reversed(self):
        test_rate1 = ExchangeRate(currency_pair='USDABC', exchange_rate=1/2)
        test_rate1.save()
        test_rate2 = ExchangeRate(currency_pair='USDDEF', exchange_rate=1/8)
        test_rate2.save()
        url=('/currency/ABC/DEF/')
        response = self.client.get(url, format='json')
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data, [{'currency_pair':'ABCDEF', 'exchange_rate':1/4}])

    def test_request_both_currencies_not_in_database(self):
        url=('/currency/ABC/XYZ/')
        response = self.client.get(url, format='json')
        self.assertTrue(response.status_code==status.HTTP_400_BAD_REQUEST)

    def test_request_one_currency_not_in_database(self):
        test_rate1 = ExchangeRate(currency_pair='USDABC', exchange_rate=1/2)
        test_rate1.save()
        url=('/currency/ABC/XYZ/')
        response = self.client.get(url, format='json')
        self.assertTrue(response.status_code==status.HTTP_400_BAD_REQUEST)


    def test_cant_delete_exchange_rate(self):
        url = ('/currency/ABC/XYZ/')
        response = self.client.delete(url, format='json')
        self.assertTrue(status.is_client_error(response.status_code))
        