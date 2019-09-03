"""Platzigram URL Configuration."""

from django.urls import path
from platzigram import views

urlpatterns = [
    path('hello-world/', views.hello_world),
    path('sorted', views.sort_integer),
    # path('hi/<str:>')
]
