from django.urls import path
from . import views

urlpatterns = [
    path('', views.foro, name='Foro'),
]
