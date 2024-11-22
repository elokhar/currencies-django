from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from currencies.models import *
from currencies.serializers import *

def welcome(request):
    return HttpResponse("Welcome to the exchange rate information app!")

@api_view(['GET'])
def currency_list(request):
    currencies = Currency.objects.all().order_by('code')
    serializer = CurrencySerializer(currencies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def rate_list(request, curr1, curr2):
    rate = ExchangeRate.objects.all().filter(currency_pair=curr1+curr2)
    if not rate:
        rate = ExchangeRate.objects.all().filter(currency_pair=curr2+curr1)

    serializer = ExchangeRateSerializer(rate, many=True)
    return Response(serializer.data)