from django.urls import path
from . import views
from currencies.load_exchange_rates import load_exchange_rates

load_exchange_rates()

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('currencies/', views.currency_list),
]



