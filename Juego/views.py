from django.shortcuts import render
from .models import Lienzo, Pixel
#Para las respuestas ajax en formato Json
from django.http import JsonResponse
#Para convertir un objeto de una clase en en Json
from django.core import serializers



def juego(request):
    return render(request, 'Juego/Juego.html')

def CargarGrillaAjax(request):

    # Te trae la grilla principal o te la crea     
    grillaPrincipal = Lienzo.objects.get_or_create(principal=True)
    pixeles = Pixel.objects.filter(lienzo__in = grillaPrincipal)
    datos = []

    for pixel in pixeles:
        
        dato = {
            "X": pixel.coordenadaX,
            "Y": pixel.coordenadaY,
            "color": [pixel.Red, pixel.Green, pixel.Blue, pixel.Alpha],
            "vidas": pixel.vidas,
        }

        datos.append(dato)
    return JsonResponse(datos, safe = False)




