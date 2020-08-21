from django.shortcuts import render
from django.http import HttpResponse


def miscelaneo(request):
    return HttpResponse('<h1>Esta es la pagina de Miscelaneo</h1>')

