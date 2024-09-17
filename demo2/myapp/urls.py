from django.urls import path
from . import views

urlpatterns = [
    path("", views.rsa_app ,name='rsa_app'),
    path('procesar-texto/', views.procesar_texto, name='procesar_texto')
]