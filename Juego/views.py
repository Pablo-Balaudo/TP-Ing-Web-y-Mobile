from django.shortcuts import render


def juego(request):
    return render(request, 'Juego/Juego.html')
