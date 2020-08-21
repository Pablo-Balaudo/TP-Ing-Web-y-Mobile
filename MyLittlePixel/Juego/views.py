from django.shortcuts import render
from django.http import HttpResponse


def juego(request):
    return HttpResponse('<h1>Esta es la pagina del Juego</h1>')
