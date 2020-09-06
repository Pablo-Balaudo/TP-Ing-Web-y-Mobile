from django.shortcuts import render
from .models import Lienzo, Pixel


def juego(request):

    return render(request, 'Juego/Juego.html')
