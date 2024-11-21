from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('currencies/', views.currency_list),
]
