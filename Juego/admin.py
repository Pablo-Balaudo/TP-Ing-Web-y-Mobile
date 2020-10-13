from django.contrib import admin
from Juego.models import *

class AdminPixeles(admin.ModelAdmin):
    # Los campos que mostrara el admin al navegar entre los Objetos
    list_display = ("lienzo", "coordenadaX", "coordenadaY",)
    # Los campos que por los que admin te permitirá filtrar los Objetos
    list_filter = ("owner",)
    # Los campos que por los que admin te permitirá Buscar los Objetos
    search_fields = ("coordenadaX", "coordenadaY",)


admin.site.register(Pixel, AdminPixeles)


class AdminLienzos(admin.ModelAdmin):
    # Los campos que mostrara el admin al navegar entre los Objetos
    list_display = ("fechainicio",)
    # Los campos que por los que admin te permitirá Buscar los Objetos
    search_fields = ("fechainicio",)
    # Para establecer una jerarquia de fecha
    date_hierarchy = "fechainicio"


admin.site.register(Lienzo, AdminLienzos)


class AdminColores(admin.ModelAdmin):
    # Los campos que mostrara el admin al navegar entre los Objetos
    list_display = ("Nombre", "Red", "Green", "Blue", "Alpha",)
    # Los campos que por los que admin te permitirá Buscar los Objetos
    search_fields = ("Nombre",)


admin.site.register(Color, AdminColores)


class AdminJugadas(admin.ModelAdmin):
    # Los campos que mostrara el admin al navegar entre los Objetos
    list_display = ("pixel", "jugador", "color", "fecha_creacion",)
    # Los campos que por los que admin te permitirá Buscar los Objetos
    search_fields = ("pixel", "jugador", "color", )
    # Para establecer una jerarquia de fecha
    date_hierarchy = "fecha_creacion"


admin.site.register(Jugada, AdminJugadas)


class AdminDenunciasJugadasHeader(admin.ModelAdmin):
    # Los campos que mostrara el admin al navegar entre los Objetos
    list_display = ("idDenunciaJugada", "author", "fecha_creacion",)
    # Los campos que por los que admin te permitirá Buscar los Objetos
    search_fields = ("author", "text", "color", )
    # Para establecer una jerarquia de fecha
    date_hierarchy = "fecha_creacion"


admin.site.register(DenunciaJugadasHeader, AdminDenunciasJugadasHeader)

class AdminDenunciasJugadasDetail(admin.ModelAdmin):
    # Los campos que mostrara el admin al navegar entre los Objetos
    list_display = ("Header", "jugada",)
    # Los campos que por los que admin te permitirá Buscar los Objetos
    search_fields = ("Header", "jugada", )

admin.site.register(DenunciaJugadasDetail, AdminDenunciasJugadasDetail)
