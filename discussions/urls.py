"""Define URL patterns for discussions."""

from django.urls import path

from . import views

app_name = 'discussions'
urlpatterns = [
        path('', views.index, name='index'),
        path('topics/', views.topics, name='topics'),
        ]
