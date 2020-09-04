from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
#Para los formularios
from django import forms
from django.contrib.auth.forms import UserCreationForm



class Usuario(User):


    

    class Meta:
        proxy = True





class Grupo(models.Model):
    id = models.AutoField(primary_key=True)
    fechainicio = models.DateTimeField()
    fechafin = models.DateTimeField()
    guardado = models.BooleanField(default=False)
    bloqueado = models.BooleanField(default=False)


class UserRegisterForm(UserCreationForm):    
    username = forms.CharField(label='', max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}))
    email = forms.EmailField(label='', max_length=40, widget=forms.TextInput(attrs={'placeholder': 'Correo electrónico'}))
    password1 = forms.CharField(label='',min_length=8,max_length=20,widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))
    password2 = forms.CharField(label='',min_length=8,max_length=20,widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar contraseña'}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']





