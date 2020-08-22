from django.shortcuts import render


def foro(request):
    return render(request, 'Foro/Foro.html')

