from django.db import models

import datetime
from django.core.validators import MinValueValidator, MaxValueValidator

from django.contrib.auth.models import User

#Para definir metodos que se ejecuten tras la creacion de on objeto de una clase determinada 
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

#La cantidad total de pixeles es de CanvasSize x CanvasSize (Ej: si CanvasSize = 50, entonces hay 50x50 pixeles)
CanvasSize = 51



class Lienzo(models.Model):

    idLienzo = models.AutoField(primary_key=True)
    #Fechas que indican cuando se crea y cuando se retira la grilla
    fechainicio = models.DateTimeField(auto_now_add = True)
    fechafin = models.DateTimeField(null=True, default=None)
    #Definicion de las dimenciones que tendra la grilla del lienzo (si es 50x50, se debe poner 51, por ejemplo)
    tamano_max_X = models.IntegerField(default = 51)
    tamano_max_Y = models.IntegerField(default = 51)
    #booleanos que representan el estado del lienzo
    guardado = models.BooleanField(default=False)
    principal = models.BooleanField(default=False)
    bloqueado = models.BooleanField(default=False)
 


class Color(models.Model):

    Nombre = models.CharField(max_length=40)
    
    Red = models.PositiveSmallIntegerField(default = 0, validators=[MaxValueValidator(256)])
    Green = models.PositiveSmallIntegerField(default = 0, validators=[MaxValueValidator(256)])
    Blue = models.PositiveSmallIntegerField(default = 0, validators=[MaxValueValidator(256)])
    Alpha = models.PositiveSmallIntegerField(default = 0, validators=[MaxValueValidator(256)])
          
    class Meta:
        #Defino los atributos que "en conjunto" no se peden repetir (Que no halla 2 colores iguales)
        unique_together = (("Red", "Green", "Blue", "Alpha"),)



class Pixel(models.Model):

    #Para diferenciar/identificar los pixeles los unos de los otros
    coordenadaX = models.IntegerField(default = 0, validators=[MaxValueValidator(CanvasSize)])
    coordenadaY = models.IntegerField(default = 0, validators=[MaxValueValidator(CanvasSize)])
    lienzo = models.ForeignKey(Lienzo, on_delete = models.CASCADE, blank=True)
    
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



class Jugada(models.Model):
    pixel = models.ForeignKey(Pixel, on_delete = models.CASCADE)
    jugador = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    color = models.ForeignKey(Color, on_delete = models.CASCADE)



# Para que se creen los pixeles automaticamente tras crear un lienzo
@receiver(post_save, sender=Lienzo)
def crear_pixeles(sender, instance, created, **kwargs):
    if created:
        for X in range(CanvasSize):
            for Y in range(CanvasSize):
                pixel = Pixel(coordenadaX = X, coordenadaY = Y, lienzo = instance)
                pixel.save()

#Para que, al crearse una nueva jugada, el cambio se vea reflejado directamente sobre el pixel que referencia
@receiver(post_save, sender=Jugada)
def realizar_jugada(sender, instance, created, **kwargs):
    if created:
        Pixel.objects.get(instance.pixel.coordenadaX, instance.pixel.coordenadaY, instance.pixel.lienzo)


        





  
           
