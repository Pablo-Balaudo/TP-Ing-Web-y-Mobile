from django.shortcuts import render
from django.http import HttpResponse


def galeria(request):
    return HttpResponse('<h1>Esta es la pagina de la Galeria</h1>')

