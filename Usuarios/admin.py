from django.contrib import admin
from Usuarios.models import Usuario


class AdminUsuarios(admin.ModelAdmin):
    # Los campos que mostrara el admin al navegar entre los usuarios
    list_display = ("user", "FechaRegistro",)
    # Los campos que por los que admin te permitirá filtrar los usuarios
    list_filter = ("PixelOfLife", "WeAreLegion",)
    # Los campos que por los que admin te permitirá Buscar los usuarios
    search_fields = ("user",)
    # Para establecer una jerarquia de fecha
    date_hierarchy = "FechaRegistro"


admin.site.register(Usuario, AdminUsuarios)
