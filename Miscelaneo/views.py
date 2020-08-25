from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login as do_login


def miscelaneo(request):
    formulario = UserCreationForm()
    if request.method == "POST":
        # el usuario está mandando sus datos
        formulario = UserCreationForm(data=request.POST)
        if formulario.is_valid():
            usuario = formulario.save()
            # Si el usuario se crea correctamente 
            if usuario is not None:
                do_login(request, usuario)
                return render(request, 'Miscelaneo/Miscelaneo.html')

    # eliminamos el exceso de texto ayuda que se genera automaticamente
    formulario.fields['username'].help_text = None
    formulario.fields['password1'].help_text = None
    formulario.fields['password2'].help_text = None

    return render(request, "Miscelaneo/registrarse.html", {'formulario': formulario})

