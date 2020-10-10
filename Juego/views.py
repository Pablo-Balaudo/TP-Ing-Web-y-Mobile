from datetime import datetime
import pytz
# Para manejar el los archivos Json 
from django.http import JsonResponse
import json
from .models import Lienzo, Pixel, Jugada, Color
from django.shortcuts import render


def juego(request):
    return render(request, 'Juego/Juego.html')


def realizar_jugada_ajax(request):

    if request.method == 'POST':

        if datetime.now(pytz.UTC) >= request.user.usuario.FechaJuego:

            datos_recibidos = json.loads(request.body.decode("utf-8"))

            color = Color.objects.get(
                Red=datos_recibidos["Color"][0],
                Green=datos_recibidos["Color"][1],
                Blue=datos_recibidos["Color"][2],
                Alpha=datos_recibidos["Color"][3])

            jugador = request.user

            pixel = Pixel.objects.get(coordenadaX=datos_recibidos["x"], coordenadaY=datos_recibidos["y"])

            Jugada.objects.create(color=color, pixel=pixel, jugador=jugador)

            Resultado = {"Resultado": True,
                "Espera": request.user.usuario.FechaJuego, 
                "Color": datos_recibidos["Color"], 
                "X":datos_recibidos["x"], 
                "Y":datos_recibidos["y"]}   
        else:
            Resultado = {"Resultado": False, "Espera": request.user.usuario.FechaJuego}
    else:
        Resultado = {"Resultado": False, "Error": "Se debería estar enviando un POST, no un GET"}
    
    return JsonResponse(Resultado)



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


def cargar_jugadas_ajax(request):
    
    if request.method == 'POST':
        
        datos_recibidos = json.loads(request.body.decode("utf-8"))
        #Time = fecha y hora de la ultima vez que el usuario actualizó la grilla de su HTML
        Time = datetime.strptime(datos_recibidos["time"][0:28],'%a %b %d %Y %X %Z')
        Time = Time.replace(tzinfo=pytz.UTC)
        print(Time) 
        hora_actual = datetime.now(pytz.UTC)
        print(hora_actual)
        jugadas = Jugada.objects.filter(fecha_creacion__range=[Time, hora_actual])

        datos = []

        for jugada in jugadas:

            pixel = jugada.pixel
            color = jugada.color
            
            dato = {
                "X": pixel.coordenadaX,
                "Y": pixel.coordenadaY,
                "color": [color.Red, color.Green, color.Blue, color.Alpha],
                "vidas": pixel.vidas,
            }
            
            datos.append(dato)
        
        print(datos)
        return JsonResponse(datos, safe=False)
    else:
        return JsonResponse({"Resultado": False, "Error": "Se debería estar enviando un POST, no un GET"})


