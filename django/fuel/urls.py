# fuel/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('active-city/', views.ActiveCityView.as_view(), name='active-city'),
    path('fuel/', views.FuelPriceView.as_view(), name='fuel'),
]
