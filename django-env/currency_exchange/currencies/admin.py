from django.contrib import admin
from .models import *
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.
class ExchangeRateAdmin(SimpleHistoryAdmin):
  list_display = ("currency_pair", "exchange_rate",)

admin.site.register(Currency)
admin.site.register(ExchangeRate, ExchangeRateAdmin)