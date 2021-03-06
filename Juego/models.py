from datetime import timedelta, datetime

import pytz
from django.core.validators import MaxValueValidator
from django.db import models
# Para definir metodos que se ejecuten tras la creacion de on objeto de una clase determinada
from django.db.models.signals import post_save
from django.dispatch import receiver

from Usuarios.models import Denuncia, Usuario

# Estados
# STATUS_LIENZO = (
#    (1, 'Actual'),
#   (2, 'Suspendido'),
# )

# La cantidad total de pixeles es de CanvasSize x CanvasSize (Ej: si CanvasSize = 50, entonces hay 50x50 pixeles)
CanvasSize = 51


class Lienzo(models.Model):
    idLienzo = models.AutoField(primary_key=True)
    # Fechas que indican cuando se crea y cuando se retira la grilla
    fechainicio = models.DateTimeField(auto_now_add=True)
    fechafin = models.DateTimeField(null=True, default=None)
    # Definicion de las dimenciones que tendra la grilla del lienzo (si es 50x50, se debe poner 51, por ejemplo)
    tamano_max_X = models.IntegerField(default=51)
    tamano_max_Y = models.IntegerField(default=51)
    # booleanos que representan el estado del lienzo
    principal = models.BooleanField(default=False)

    # Estado_Lienzo = models.IntegerField(choices=STATUS_LIENZO)

    def limpiar_lienzo(self):
        color_default = Color.objects.get(Nombre="black", Red=0, Green=0, Blue=0, Alpha=1)
        Pixel.objects.filter(lienzo=self).update(color=color_default, vidas=1, owner=None)


class Color(models.Model):
    Nombre = models.CharField(max_length=30)

    Red = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(256)])
    Green = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(256)])
    Blue = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(256)])
    Alpha = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(256)])

    def __str__(self):
        rgba = f' [{self.Red:d}, {self.Green:d}, {self.Blue:d}, {self.Alpha:d}]'
        return self.Nombre + rgba

    class Meta:
        # Defino los atributos que "en conjunto" no se peden repetir (Que no halla 2 colores iguales)
        unique_together = [["Nombre"], ["Red", "Green", "Blue", "Alpha"]]


class Pixel(models.Model):
    # Para diferenciar/identificar los pixeles los unos de los otros
    coordenadaX = models.IntegerField(default=0, validators=[MaxValueValidator(CanvasSize)])
    coordenadaY = models.IntegerField(default=0, validators=[MaxValueValidator(CanvasSize)])
    lienzo = models.ForeignKey(Lienzo, on_delete=models.CASCADE, blank=True)

    color = models.ForeignKey(Color, on_delete=models.SET_NULL, blank=True, null=True)

    # Datos propios del juego
    vidas = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(5)])
    owner = models.ForeignKey('auth.User', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return '({0}, {1})'.format(self.coordenadaX, self.coordenadaY)

    class Meta:
        # Defino los atributos que "en conjunto" no se peden repetir
        unique_together = (("coordenadaX", "coordenadaY", "lienzo"),)


class Jugada(models.Model):
    pixel = models.ForeignKey(Pixel, on_delete=models.CASCADE)
    jugador = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def aplicar_jugada(self):
        Pixel.objects.filter(
            coordenadaX=self.pixel.coordenadaX,
            coordenadaY=self.pixel.coordenadaY
        ).update(
            color=self.color,
            owner=self.jugador
        )

    def __str__(self):
        return '{0} - {1} - {2}'.format(self.pixel, self.jugador, self.fecha_creacion)

    class Meta:
        ordering = ['-fecha_creacion']


class DenunciaJugadasHeader(Denuncia):
    idDenunciaJugada = models.AutoField(primary_key=True)


class DenunciaJugadasDetail(models.Model):
    Header = models.ForeignKey(DenunciaJugadasHeader, on_delete=models.CASCADE)
    jugada = models.ForeignKey(Jugada, on_delete=models.CASCADE)


# Para que se creen los pixeles automaticamente tras crear un lienzo
@receiver(post_save, sender=Lienzo)
def crear_pixeles(sender, instance, created, **kwargs):
    if created:
        for X in range(1, CanvasSize):
            for Y in range(1, CanvasSize):
                pixel = Pixel(
                    coordenadaX=X,
                    coordenadaY=Y,
                    lienzo=instance,
                    color=Color.objects.get(Nombre="black", Red=0, Green=0, Blue=0, Alpha=1)
                )
                pixel.save()


# Para que, al crearse una nueva jugada, el cambio se vea reflejado directamente sobre el pixel que referencia
@receiver(post_save, sender=Jugada)
def realizar_jugada(sender, instance, created, **kwargs):
    if created:
        instance.aplicar_jugada()
        nuevo_tiempo_espera = datetime.now(pytz.UTC) + timedelta(minutes=1)
        Usuario.objects.filter(user=instance.jugador).update(FechaJuego=nuevo_tiempo_espera)
