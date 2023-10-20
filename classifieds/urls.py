"""Defines URL patterns for classifieds."""

from django.urls import path
from . import views

app_name = 'classifieds'

urlpatterns = [
        path('', views.index, name='index'),
        ]
