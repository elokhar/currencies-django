from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from currencies.models import Currency
from currencies.serializers import CurrencySerializer

def welcome(request):
    return HttpResponse("Welcome to the exchange rate information app!")

@api_view(['GET'])
def currency_list(request):
    currencies = Currency.objects.all().order_by('code')
    serializer = CurrencySerializer(currencies, many=True)
    return Response(serializer.data)