from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Para el registro
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .utils import generate_token
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from django.conf import settings
import urllib
import json


def send_email_activation(user, email, request):
    current_site = str(get_current_site(request))
    mail_subject = 'Activa tu cuenta en MyLittlePixel'
    message = render_to_string('Usuarios/Activation.html',
                               {
                                   'user': user,
                                   'domain': current_site,
                                   'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                                   'token': generate_token.make_token(user)
                               }
                               )

    return EmailMessage(
        mail_subject,
        message,
        settings.EMAIL_HOST_USER,
        [email]
    )


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']

            # RECAPTCHA
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req = urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())

            # MENSAJES DE ERROR
            bandera = False
            if not result['success']:      
                form.add_error(None, 'reCAPTCHA inválido. Inténtelo de nuevo.')
                bandera = True
            if User.objects.filter(email=email).exists():
                form.add_error(None, 'Correo electrónico en uso, elige otro.')
                bandera = True

            # ¿HAY MENSAJES DE ERROR?
            if bandera:
                return render(request, 'Usuarios/Register.html', {'form': form}, status=400)
            else:
                user = form.save(commit=False)
                user.is_active = False
                user.save()

                email_message = send_email_activation(user, email, request)
                email_message.send(fail_silently=False)

                messages.success(request, f'¡Tu cuenta ha sido creada! Se ha enviado un correo para la activación de '
                                          f'su cuenta')
                return redirect('/login')
    else:
        form = UserRegisterForm()

    # eliminamos el exceso de texto ayuda que se genera automaticamente
    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None

    return render(request, 'Usuarios/Register.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

        # Si el usuario ya está activo lo manda directo al login
        if user.is_active:
            return redirect('/login')

        user.is_active = True
        user.save()
        return render(request, 'Usuarios/Email_activation.html')
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    return render(request, 'Usuarios/Email_activation_failed.html')


def resendverification(request):
    if request.method == 'POST':
        form = Resendverification(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if not User.objects.filter(email=email).exists():
                form.add_error(None, 'Correo electrónico incorrecto.')
                return render(request, 'Usuarios/Resendverification.html', {'form': form}, status=400)
            else:
                user = User.objects.get(email=email)
                email_message = send_email_activation(user, email, request)
                email_message.send(fail_silently=False)

                messages.success(request, f'Se ha reenviado un correo para la activación de su cuenta!')
                return redirect('/login')
    else:
        form = Resendverification()

    return render(request, 'Usuarios/Resendverification.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'Usuarios/Profile.html')
