from django.contrib import admin
from .models import *

# Register your models here.
class ExchangeRateAdmin(admin.ModelAdmin):
  list_display = ("currency_pair", "exchange_rate",)

admin.site.register(Currency)
admin.site.register(ExchangeRate, ExchangeRateAdmin)