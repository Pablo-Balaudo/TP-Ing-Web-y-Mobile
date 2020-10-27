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
    actions = ['reiniciar_lienzo', 'vaciar_lienzo']

    # Metodo para re-aplicar las jugadas existentes a la grilla
    def reiniciar_lienzo(self, request, queryset):
        for lienzo in queryset:
            lienzo.limpiar_lienzo()
            jugadas = Jugada.objects.all().order_by('fecha_creacion')
            for jugada in jugadas:
                jugada.aplicar_jugada()

    reiniciar_lienzo.short_description = 'Reiniciar lienzo (without Delete of Jugadas)'

    # Metodo para dejar el lienzo en planco y borrar toda jugada realizada sobre esta
    def vaciar_lienzo(self, request, queryset):
        for lienzo in queryset:
            lienzo.limpiar_lienzo()
            Jugada.objects.all().delete()

    vaciar_lienzo.short_description = 'Reformatear lienzo (with Delete of Jugadas)'


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
    list_display = ("idDenunciaJugada", "author", "fecha_creacion", "aplicada",)
    # Los campos que por los que admin te permitirá Buscar los Objetos
    search_fields = ("author", "text", "color",)
    # Los campos que por los que admin te permitirá filtrar los usuarios
    list_filter = ("aplicada",)
    # Para establecer una jerarquia de fecha
    date_hierarchy = "fecha_creacion"
    # Metodos a aplicar sobre los registros que selecciones
    actions = ['aplicar_medidas']

    # Metodo para eliminar las jugadas asociadas a las denuncias seleccionadas 
    def aplicar_medidas(self, request, queryset):
        for denunciaHeader in queryset:

            identificador = denunciaHeader.idDenunciaJugada
            DenunciaJugadasHeader.objects.filter(idDenunciaJugada=identificador).update(aplicada=True)

            denuncias_details = DenunciaJugadasDetail.objects.filter(Header=denunciaHeader)
            for denunciaDetail in denuncias_details:
                instance = denunciaDetail.jugada
                instance.delete()

            lienzo = Lienzo.objects.get(principal=True)
            lienzo.limpiar_lienzo()

            jugadas = Jugada.objects.all().order_by('fecha_creacion')
            for jugada in jugadas:
                jugada.aplicar_jugada()

    change_form_template = 'Juego/Denuncia.html'

    aplicar_medidas.short_description = 'Eliminar Jugadas Implicadas'


admin.site.register(DenunciaJugadasHeader, AdminDenunciasJugadasHeader)


class AdminDenunciasJugadasDetail(admin.ModelAdmin):
    # Los campos que mostrara el admin al navegar entre los Objetos
    list_display = ("Header", "jugada",)
    # Los campos que por los que admin te permitirá Buscar los Objetos
    search_fields = ("Header", "jugada",)


admin.site.register(DenunciaJugadasDetail, AdminDenunciasJugadasDetail)
