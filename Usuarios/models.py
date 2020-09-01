from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Usuario(User):


    

    class Meta:
        proxy = True


class Pixel(models.Model):
    color = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(255)])
    vidas = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(5)])
    coordenadaX = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(50)])
    coordenadaY = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(50)])
    #clave foranea
    dueño = models.ForeignKey('auth.User', models.SET_NULL, blank=True, null=True,)




class Lienzo(models.Model):
    id = models.AutoField(primary_key=True)
    fechainicio = models.DateTimeField()
    fechafin = models.DateTimeField()
    guardado = models.BooleanField(default=False)
    bloqueado = models.BooleanField(default=False)











