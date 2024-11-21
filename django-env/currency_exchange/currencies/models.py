from django.db import models

class Currency(models.Model):
    code = models.CharField(max_length=3)
    reverse_rate = models.BooleanField(default=False)
    exchange_rate = models.FloatField(default=0)

class ExchangeRate(models.Model):
    currency_pair = models.CharField(max_length=6)
    exchangeRate = models.FloatField(default=0)