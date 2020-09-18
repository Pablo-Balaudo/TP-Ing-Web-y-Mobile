from django.db import models
import datetime

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

#La cantidad total de pixeles es de CanvasSize x CanvasSize (Ej: si CanvasSize = 50, entonces hay 50x50 pixeles)
CanvasSize = 51


class Lienzo(models.Model):
    idLienzo = models.AutoField(primary_key=True)
    fechainicio = models.DateTimeField(auto_now_add = True)
    fechafin = models.DateTimeField(null=True, default=None)
    guardado = models.BooleanField(default=False)
    principal = models.BooleanField(default=False)
    bloqueado = models.BooleanField(default=False)


class Pixel(models.Model):

    #Para diferenciar/identificar los pixeles los unos de los otros
    coordenadaX = models.IntegerField(default = 0, validators=[MaxValueValidator(CanvasSize)])
    coordenadaY = models.IntegerField(default = 0, validators=[MaxValueValidator(CanvasSize)])
    lienzo = models.ForeignKey(Lienzo, on_delete = models.CASCADE, null = True)
    
    #para determinar el color
    Red = models.PositiveSmallIntegerField(default = 0, validators=[MaxValueValidator(256)])
    Green = models.PositiveSmallIntegerField(default = 0, validators=[MaxValueValidator(256)])
    Blue = models.PositiveSmallIntegerField(default = 0, validators=[MaxValueValidator(256)])
    Alpha = models.PositiveSmallIntegerField(default = 0, validators=[MaxValueValidator(256)])
    
    #Datos propios del juego
    vidas = models.PositiveIntegerField(default = 1, validators=[MaxValueValidator(5)])
    dueño = models.ForeignKey('auth.User', models.SET_NULL, blank=True, null=True)

    class Meta:
        #Defino los atributos que "en conjunto" no se peden repetir
        unique_together = (("coordenadaX", "coordenadaY", "lienzo"),)



# Para que se creen los pixeles automaticamente tras crear un lienzo
@receiver(post_save, sender=Lienzo)
def crear_pixeles(sender, instance, created, **kwargs):
    if created:
        for X in range(CanvasSize):
            for Y in range(CanvasSize):
                pixel = Pixel(coordenadaX = X, coordenadaY = Y, lienzo = instance)
                pixel.save()
  
           
