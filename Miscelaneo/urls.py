from django.urls import path
from . import views

urlpatterns = [
    path('', views.miscelaneo, name='Miscelaneo'),
]