# Para manejar el los archivos Json
import json

from django.http import JsonResponse
from django.shortcuts import render

from .models import *


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
            pixel = Pixel.objects.get(coordenadaX=datos_recibidos["x"], coordenadaY=datos_recibidos["y"])
            jugador = request.user

            Jugada.objects.create(color=color, pixel=pixel, jugador=jugador)
            tiempo_espera = timedelta(minutes=1).seconds

            resultado = {"Resultado": True,
                         "Espera": tiempo_espera,
                         "Color": datos_recibidos["Color"],
                         "X": datos_recibidos["x"],
                         "Y": datos_recibidos["y"]}
        else:
            tiempo_espera = request.user.usuario.segundos_espera()
            resultado = {"Resultado": False, "Espera": tiempo_espera}
    else:
        resultado = {"Resultado": False, "Error": "Se debería estar enviando un POST, no un GET"}

    return JsonResponse(resultado)


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
    if request.method == 'GET':
        datos_recibidos = request.GET["time"]
        # time = fecha y hora de la ultima vez que el usuario actualizó la grilla de su HTML
        time = datetime.strptime(datos_recibidos[0:28], '%a %b %d %Y %X %Z')
        time = time.astimezone(pytz.utc)
        hora_actual = datetime.now(pytz.UTC)
        jugadas = Jugada.objects.filter(fecha_creacion__range=[time, hora_actual])

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

        return JsonResponse(datos, safe=False)
    else:
        return JsonResponse({"Resultado": False, "Error": "Se debe enviar un GET, no un POST"})


def realizar_denuncia_ajax(request):
    if request.method == 'POST':

        datos_recibidos = json.loads(request.body.decode("utf-8"))
        time = datetime.strptime(datos_recibidos["time"][0:28], '%a %b %d %Y %X %Z')
        time = time.astimezone(pytz.utc)

        denuncia = DenunciaJugadasHeader.objects.create(author=request.user,
                                                        fecha_creacion=time,
                                                        text=datos_recibidos["text"])

        no_existen_jugadas = True

        for index in datos_recibidos["pixeles"]:

            pixel = Pixel.objects.get(coordenadaX=index["x"], coordenadaY=index["y"])
            hay_jugada = Jugada.objects.filter(pixel=pixel).exists()

            if hay_jugada:
                no_existen_jugadas = False
                jugada = Jugada.objects.filter(pixel=pixel).order_by('-fecha_creacion').first()
                DenunciaJugadasDetail.objects.create(Header=denuncia, jugada=jugada)
            else:
                print("se realizo una denuncia a un pixel sin dueño")

        if no_existen_jugadas:
            denuncia.delete()

        resultado = {"Resultado": True}
    else:
        resultado = {"Resultado": False, "Error": "Se debería estar enviando un POST, no un GET"}

    return JsonResponse(resultado)


def obtener_denuncia_ajax(request):
    if request.method == 'GET':

        datos_recibidos = request.GET["id"]

        denuncia = DenunciaJugadasHeader.objects.get(id=datos_recibidos)

        DenunciasDetails = DenunciaJugadasDetail.objects.filter(Header=denuncia)

        datos = []

        for DenunciaDetail in DenunciasDetails:
            pixel = DenunciaDetail.jugada.pixel
            color = DenunciaDetail.jugada.color

            dato = {
                "X": pixel.coordenadaX,
                "Y": pixel.coordenadaY,
                "color": [color.Red, color.Green, color.Blue, color.Alpha],
                "vidas": pixel.vidas,
            }

            datos.append(dato)

        return JsonResponse(datos, safe=False)
    else:
        return JsonResponse({"Resultado": False, "Error": "Se debe enviar un GET, no un POST"})


def consultar_tiempo_espera_ajax(request):
    if request.method == 'GET':
        tiempo_espera = request.user.usuario.segundos_espera()
        resultado = {"Resultado": True, "Espera": tiempo_espera}
    else:
        resultado = {"Resultado": False, "Error": "Se debería estar enviando un GET, no un POST"}

    return JsonResponse(resultado)
