from django.db import models

from datetime import timedelta, datetime

# Para la extencion de la clase User
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

# Para los formularios
from django import forms
from django.contrib.auth.forms import UserCreationForm


# Aqui se ubican los posibles tiempos de espera:

tiempo_espera_1 = timedelta(seconds=15)
tiempo_espera_2 = timedelta(hours=24)
tiempo_espera_3 = timedelta(hours=12)
tiempo_espera_4 = timedelta(hours=6)
tiempo_espera_5 = timedelta(hours=3)

# Estados
#STATUS_USERS = (
#    (1, 'Pendiente de verificacion'),
#    (2, 'Activo'),
#    (3, 'Bloqueado'),
#    (4, 'Eliminado'),
#)

#ASIGNATION_MOD = (
#    (1, 'Moderador'),
#    (2, 'Sugerido'),
#    (3, 'Normal'),
#)

class Usuario(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)    
    
    FechaRegistro = models.DateTimeField(auto_now_add=True)
    # El tiempo de espera figura en minutos
    cooldown = models.DurationField(blank=True, null=True)    
    # Fecha a partir de la cual puede pintar otra vez
    FechaJuego = models.DateTimeField(auto_now_add=True)  

    Puntos = models.IntegerField(default=0)
    WeAreLegion = models.BooleanField(default=False)
    PixelOfLife = models.BooleanField(default=False)
    # Estado_Usuario = models.IntegerField(choices=STATUS_USERS)
    # Estado_Moderador = models.IntegerField(choices=ASIGNATION_MOD)

    def DefinirEspera(self):
        self.TiempoEspera = tiempo_espera_1                   
        self.FechaJuego = datetime.now() + self.TiempoEspera




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


# Esto es semejante a los eventos y delegados, permitiendo que al crearse un user, automaticamente se cree un usuario
# asociado
@receiver(post_save, sender=User)
def crear_usuario(sender, instance, created, **kwargs):
    if created:
        Usuario.objects.create(user=instance)


@receiver(post_save, sender=User)
def guardar_usuario(sender, instance, **kwargs):
    instance.usuario.save()
