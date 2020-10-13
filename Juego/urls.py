from django.urls import path
from . import views

urlpatterns = [
    path('', views.juego, name='Juego'),
    path('', views.juego, name='Juego'),
]
