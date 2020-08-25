from django.shortcuts import render


def juego(request):
    return render(request, 'Juego/Juego.html')


def login(request):
    return render(request, 'Juego/Login.html')


def register(request):
    return render(request, 'Juego/Register.html')


def forgotpassword(request):
    return render(request, 'Juego/Forgotpassword.html')


def resendverification(request):
    return render(request, 'Juego/Resendverification.html')
