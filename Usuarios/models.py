from django.db import models

import datetime
# from datetime import timedelta
# Para la extencion de la clase User
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
# Para los formularios
from django import forms
from django.contrib.auth.forms import UserCreationForm


class Usuario(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    FechaRegistro = models.DateTimeField(auto_now_add = True)
    # El tiempo de espera figura en minutos
    # TiempoEspera = models.DurationField(default = timedelta(days=1))
    Puntos = models.IntegerField(default=0)
    # Fecha a partir de la cual puede pintar otra vez
    # FechaJuego = models.DateTimeField(default=FechaRegistro)
    WeAreLegion = models.BooleanField(default=False)
    PixelOfLife = models.BooleanField(default=False)
    Conectado = models.BooleanField(default=False)
    Baneado = models.BooleanField(default=False)



class UserRegisterForm(UserCreationForm):
    
    username = forms.CharField(label='', max_length=20,
    widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}))

    email = forms.EmailField(label='', max_length=40,
    widget=forms.TextInput(attrs={'placeholder': 'Correo electrónico'}))

    password1 = forms.CharField(label='', min_length=8, max_length=20,
    widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))

    password2 = forms.CharField(label='', min_length=8, max_length=20,
    widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar contraseña'}))


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class Resendverification(UserCreationForm):
    email = forms.EmailField(label='', max_length=40,
                             widget=forms.TextInput(attrs={'placeholder': 'Correo electrónico'}))

    def __init__(self, *args, **kwargs):
        super(Resendverification, self).__init__(*args, **kwargs)
        self.fields.pop('username')
        self.fields.pop('password1')
        self.fields.pop('password2')



#Esto es semejante a los eventos y delegados, permitiendo que al crearse un user, automaticamente se cree un usuario asociado
@receiver(post_save, sender=User)
def crear_usuario(sender, instance, created, **kwargs):
    if created:
        Usuario.objects.create(user=instance)

@receiver(post_save, sender=User)
def guardar_usuario(sender, instance, **kwargs):
    instance.usuario.save()