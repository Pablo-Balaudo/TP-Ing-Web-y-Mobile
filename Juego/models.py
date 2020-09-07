from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator, MaxValueValidator

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


CanvasSize = 51


class Lienzo(models.Model):
    id = models.AutoField(primary_key=True)
    # fechainicio = models.DateTimeField()
    # fechafin = models.DateTimeField()
    guardado = models.BooleanField(default=False)
    bloqueado = models.BooleanField(default=False)


class Pixel(models.Model):
    color = ArrayField(models.PositiveIntegerField(default=0, validators=[MaxValueValidator(255)]), size=4)
    vidas = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(5)])

    lienzo = models.ForeignKey(Lienzo, on_delete=models.CASCADE, null=True)
    coordenadaX = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(CanvasSize)])
    coordenadaY = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(CanvasSize)])

    clave_primaria = [coordenadaX, coordenadaY, lienzo]

    owner = models.ForeignKey('auth.User', models.SET_NULL, blank=True, null=True)


# Para que se creen los pixeles automaticamente tras crear un lienzo


@receiver(post_save, sender=Lienzo)
def crear_pixeles(sender, instance, created, **kwargs):
    if created:
        for X in range(CanvasSize):
            for Y in range(CanvasSize):
                Pixel.objects.create(coordenadaX=X, coordenadaY=Y, lienzo=instance)


@receiver(post_save, sender=Lienzo)
def guardar_pixeles(sender, instance, **kwargs):
    instance.pixel.save()    
