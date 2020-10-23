from django.contrib import admin

from .models import Post, Comment, DenunciaPost, DenunciaComment


class AdminPost(admin.ModelAdmin):
    # Los campos que mostrara el admin al navegar entre los Objetos
    list_display = ("title", "date_posted", "author", "active")

    list_filter = ("title", "text", "date_posted", "author", "active")
    # Los campos que por los que admin te permitirá Buscar los Objetos
    search_fields = ["title", "text", ]
    # Para establecer una jerarquia de fecha
    date_hierarchy = "date_posted"


admin.site.register(Post, AdminPost)


class AdminComment(admin.ModelAdmin):
    # Los campos que mostrara el admin al navegar entre los Objetos
    list_display = ("post", "date_posted", "author", "active")

    list_filter = ("post", "text", "date_posted", "author", "active")
    # Los campos que por los que admin te permitirá Buscar los Objetos
    search_fields = ["text", ]
    # Para establecer una jerarquia de fecha
    date_hierarchy = "date_posted"


admin.site.register(Comment, AdminComment)


class AdminDenunciaPost(admin.ModelAdmin):
    list_display = ("post", "author", "text", "fecha_creacion")
    list_filter = ("post", "fecha_creacion", "author")
    # Para establecer una jerarquia de fecha
    date_hierarchy = "fecha_creacion"


admin.site.register(DenunciaPost, AdminDenunciaPost)


class AdminDenunciaComment(admin.ModelAdmin):
    list_display = ("comment", "author", "text", "fecha_creacion")
    list_filter = ("comment", "fecha_creacion", "author")
    # Para establecer una jerarquia de fecha
    date_hierarchy = "fecha_creacion"


admin.site.register(DenunciaComment, AdminDenunciaComment)
