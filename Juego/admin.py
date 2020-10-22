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
    # Metodos a aplicar sobre los registros que selecciones
    actions = ['ReiniciarLienzo', 'VaciarLienzo']
    
    # Metodo para re-aplicar las jugadas existentes a la grilla
    def ReiniciarLienzo(self, request, queryset):
        for lienzo in queryset:
            lienzo.limpiarLienzo()
            jugadas = Jugada.objects.all().order_by('fecha_creacion')
            for jugada in jugadas:
                jugada.aplicarJugada()
    ReiniciarLienzo.short_description = 'Reiniciar lienzo (without Delete of Jugadas)'

    # Metodo para dejar el lienzo en planco y borrar toda jugada realizada sobre esta
    def VaciarLienzo(self, request, queryset):
        for lienzo in queryset:
            lienzo.limpiarLienzo()
            Jugada.objects.all().delete()
    VaciarLienzo.short_description = 'Reformatear lienzo (with Delete of Jugadas)'

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
    search_fields = ("pixel", "jugador", "color",)
    # Para establecer una jerarquia de fecha
    date_hierarchy = "fecha_creacion"

admin.site.register(Jugada, AdminJugadas)


class AdminDenunciasJugadasHeader(admin.ModelAdmin):
    # Los campos que mostrara el admin al navegar entre los Objetos
    list_display = ("idDenunciaJugada", "author", "fecha_creacion",)
    # Los campos que por los que admin te permitirá Buscar los Objetos
    search_fields = ("author", "text", "color",)
    # Para establecer una jerarquia de fecha
    date_hierarchy = "fecha_creacion"
    # Metodos a aplicar sobre los registros que selecciones
    actions = ['AplicarMedidas']
    
    # Metodo para eliminar las jugadas asociadas a las denuncias seleccionadas 
    def AplicarMedidas(self, request, queryset):
        for denunciaHeader in queryset:
            denunciasDetails = DenunciaJugadasDetail.objects.filter(Header=denunciaHeader)
            for denunciaDetail in denunciasDetails:
                instance = denunciaDetail.jugada
                instance.delete()
    AplicarMedidas.short_description = 'Eliminar Jugadas Implicadas'

admin.site.register(DenunciaJugadasHeader, AdminDenunciasJugadasHeader)


class AdminDenunciasJugadasDetail(admin.ModelAdmin):
    # Los campos que mostrara el admin al navegar entre los Objetos
    list_display = ("Header", "jugada",)
    # Los campos que por los que admin te permitirá Buscar los Objetos
    search_fields = ("Header", "jugada",)

admin.site.register(DenunciaJugadasDetail, AdminDenunciasJugadasDetail)



