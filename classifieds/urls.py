"""Defines URL patterns for classifieds."""

from django.urls import path
from . import views

app_name = 'classifieds'

urlpatterns = [
        path('', views.index, name='index'),
        path('categories/', views.categories, name='categories'),
        path('categories/<int:category_id>/', views.category,name='category'),
        ]
