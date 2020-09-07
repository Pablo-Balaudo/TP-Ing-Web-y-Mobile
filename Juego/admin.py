from django.contrib import admin
from Juego.models import Pixel, Lienzo


class AdminPixeles(admin.ModelAdmin):
    list_display = ("coordenadaX","coordenadaY")

admin.site.register(Pixel, AdminPixeles)
admin.site.register(Lienzo)
