"""MICHAEL URLConfig"""
from django.urls import path
# from michael import views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Add more URL patterns as needed
]
