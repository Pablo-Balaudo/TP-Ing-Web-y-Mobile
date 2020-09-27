from django.contrib import admin
from Juego.models import Pixel, Lienzo, Jugada, Color

class AdminJugadas(admin.ModelAdmin):
    #Los campos que mostrara el admin al navegar entre los Objetos
    list_display = ("pixel", "jugador","color",)
    #Los campos que por los que admin te permitirá Buscar los Objetos
    search_fields = ("pixel", "jugador",)
admin.site.register(Jugada, AdminJugadas)
 

class AdminPixeles(admin.ModelAdmin):
    #Los campos que mostrara el admin al navegar entre los Objetos
    list_display = ("lienzo", "coordenadaX","coordenadaY",)
    #Los campos que por los que admin te permitirá filtrar los Objetos
    list_filter = ("owner",)
    #Los campos que por los que admin te permitirá Buscar los Objetos
    search_fields = ("coordenadaX","coordenadaY",)
admin.site.register(Pixel, AdminPixeles)


class AdminLienzos(admin.ModelAdmin):
    #Los campos que mostrara el admin al navegar entre los Objetos
    list_display = ("fechainicio",)
    #Los campos que por los que admin te permitirá filtrar los Objetos
    list_filter = ("guardado", "bloqueado",)
    #Los campos que por los que admin te permitirá Buscar los Objetos
    search_fields = ("fechainicio",)
    #Para establecer una jerarquia de fecha
    date_hierarchy = "fechainicio"
admin.site.register(Lienzo, AdminLienzos)


class AdminColores(admin.ModelAdmin):
    #Los campos que mostrara el admin al navegar entre los Objetos
    list_display = ("Nombre", "Red", "Green", "Blue", "Alpha",)
    #Los campos que por los que admin te permitirá Buscar los Objetos
    search_fields = ("Nombre",)
admin.site.register(Color, AdminColores)