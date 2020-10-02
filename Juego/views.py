from django.shortcuts import render
from .models import Lienzo, Pixel, Jugada, Color
# Para las respuestas ajax en formato Json
from django.http import JsonResponse
import json
# Para convertir un objeto de una clase en en Json


def juego(request):
    return render(request, 'Juego/Juego.html')


def realizar_jugada_ajax(request):

    datos_recibidos = json.loads(request.body.decode("utf-8"))

    color = Color.objects.get(
        Red=datos_recibidos["Color"][0],
        Green=datos_recibidos["Color"][1],
        Blue=datos_recibidos["Color"][2],
        Alpha=datos_recibidos["Color"][3])

    jugador = request.user

    pixel = Pixel.objects.get(coordenadaX=datos_recibidos["x"], coordenadaY=datos_recibidos["y"])

    jugada = Jugada.objects.create(color=color, pixel=pixel, jugador=jugador)
    jugada.objects.save()
    return JsonResponse({"resultado": True})


def cargar_grilla_ajax(request):

    # Te trae la grilla principal o te la crea     
    grilla_principal = Lienzo.objects.get_or_create(principal=True)
    pixeles = Pixel.objects.filter(lienzo__in=grilla_principal)
    datos = []

    for pixel in pixeles:
        dato = {
            "X": pixel.coordenadaX,
            "Y": pixel.coordenadaY,
            "color": [pixel.color.Red, pixel.color.Green, pixel.color.Blue, pixel.color.Alpha],
            "vidas": pixel.vidas,
        }

        datos.append(dato)
    return JsonResponse(datos, safe=False)
