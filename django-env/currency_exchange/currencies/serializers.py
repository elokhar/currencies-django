from currencies.models import *
from rest_framework import serializers


class CurrencySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Currency
        fields = ['code']

class ExchangeRateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExchangeRate
        fields = ['currency_pair', 'exchange_rate']

