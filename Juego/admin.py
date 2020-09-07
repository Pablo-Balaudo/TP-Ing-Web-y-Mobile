from django.contrib import admin
from Juego.models import Pixel, Lienzo



class AdminPixeles(admin.ModelAdmin):
    #Los campos que mostrara el admin al navegar entre los Objetos
    list_display = ("lienzo", "coordenadaX","coordenadaY",)
    #Los campos que por los que admin te permitirá filtrar los Objetos
    list_filter = ("dueño",)
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

