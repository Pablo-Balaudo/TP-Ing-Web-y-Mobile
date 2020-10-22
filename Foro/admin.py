from django.contrib import admin

from .models import Post, Comment


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
