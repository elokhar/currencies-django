from django.urls import path
from . import views
from currencies.load_exchange_rates import load_exchange_rates

load_exchange_rates()

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('currency/', views.currency_list),
    path('currency/<str:curr1>/<str:curr2>/', views.rate_list),
]



