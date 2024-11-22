from django.db import models
from simple_history.models import HistoricalRecords

class Currency(models.Model):
    code = models.CharField(max_length=3)
    reverse_rate = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.code}"
    class Meta:
        verbose_name_plural = "Currencies"

class ExchangeRate(models.Model):
    currency_pair = models.CharField(max_length=6)
    exchange_rate = models.FloatField(default=0)
    history = HistoricalRecords()
    def __str__(self):
        return f"{self.currency_pair}"
    