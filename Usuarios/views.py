from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Tu cuenta ha sido creada!')
            return redirect('/login')
    else:
        form = UserRegisterForm()

    # eliminamos el exceso de texto ayuda que se genera automaticamente
    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None

    return render(request, 'Usuarios/Register.html', {'form': form})


def profile(request):
    return render(request, 'Usuarios/Profile.html')
