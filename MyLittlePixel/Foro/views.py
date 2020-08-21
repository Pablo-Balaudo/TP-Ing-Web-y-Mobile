from django.shortcuts import render
from django.http import HttpResponse


def foro(request):
    return HttpResponse('<h1>Esta es la pagina del Foro</h1>')

