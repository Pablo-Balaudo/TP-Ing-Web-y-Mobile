from django.urls import path
from . import views

urlpatterns = [
    path('', views.galeria, name='Galeria'),
]