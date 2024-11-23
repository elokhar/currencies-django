from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from currencies.models import *
from currencies.serializers import *

def welcome(request):
    return HttpResponse("Welcome to the exchange rate information app!")

def get_rate_to_USD(curr):
    rate = ExchangeRate.objects.all().filter(currency_pair=curr+'USD')
    if rate:
        return rate[0].exchange_rate
    else:
        rate = ExchangeRate.objects.all().filter(currency_pair='USD'+curr)
        if rate:
            return 1.0/(rate[0].exchange_rate)
        else:
            # print(f"currency_{curr}_not_in_database")
            return None 

@api_view(['GET'])
def currency_list(request):
    currencies = Currency.objects.all().order_by('code')
    serializer = CurrencySerializer(currencies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def rate_list(request, curr1, curr2):
    if curr1 == 'USD' or curr2 == 'USD':
        rate_query_result = ExchangeRate.objects.all().filter(currency_pair=curr1+curr2)
        if not rate_query_result:
            rate_query_result = ExchangeRate.objects.all().filter(currency_pair=curr2+curr1)
        if rate_query_result:
            rate_obj = rate_query_result[0]
            if rate_obj.currency_pair != curr1 + curr2:
                rate_obj.currency_pair = curr1 + curr2
                rate_obj.exchange_rate = 1.0/rate_obj.exchange_rate
        else:
            rate_obj = None
    else:
        curr1_to_USD = get_rate_to_USD(curr1)
        curr2_to_USD = get_rate_to_USD(curr2)
        if curr1_to_USD and curr2_to_USD:
            curr1_to_curr2 = curr1_to_USD / curr2_to_USD
            rate_obj = ExchangeRate(currency_pair=curr1+curr2, exchange_rate=curr1_to_curr2)
        else:
            rate_obj = None
    if rate_obj:
        serializer = ExchangeRateSerializer([rate_obj], many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)