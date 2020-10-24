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
    actions = ['ban_posts', 'reactivate_posts', 'ban_post_author', 'reactivate_post_author']

    def ban_posts(self, request, queryset):
        """Turn selected Posts to an inactive state"""
        for post in queryset:
            post.deactivate_post()

    ban_posts.short_description = "Deactivate selected Posts"

    def reactivate_posts(self, request, queryset):
        """Turn selected Posts to an active state"""
        for post in queryset:
            post.activate_post()

    reactivate_posts.short_description = "Reactivate selected Posts"

    def ban_post_author(self, request, queryset):
        """Turn Authors of selected Posts to an inactive state"""
        for post in queryset:
            post.deactivate_post_author()

    ban_post_author.short_description = "Deactivate Authors of selected Posts"

    def reactivate_post_author(self, request, queryset):
        """Turn Authors of selected Posts to an active state"""
        for post in queryset:
            post.activate_post_author()

    reactivate_post_author.short_description = "Reactivate Authors of selected Posts"


admin.site.register(Post, AdminPost)


class AdminComment(admin.ModelAdmin):
    # Los campos que mostrara el admin al navegar entre los Objetos
    list_display = ("post", "date_posted", "author", "active")

    list_filter = ("post", "text", "date_posted", "author", "active")
    # Los campos que por los que admin te permitirá Buscar los Objetos
    search_fields = ["text", ]
    # Para establecer una jerarquia de fecha
    date_hierarchy = "date_posted"
    actions = ['ban_comments', 'reactivate_comments', 'ban_comment_author', 'reactivate_comment_author']

    def ban_comments(self, request, queryset):
        """Turn selected Comments to an inactive state"""
        for comment in queryset:
            comment.deactivate_comment()

    ban_comments.short_description = "Deactivate selected Comments"

    def reactivate_comments(self, request, queryset):
        """Turn selected Comments to an active state"""
        for comment in queryset:
            comment.activate_comment()

    reactivate_comments.short_description = "Reactivate selected Comments"

    def ban_comment_author(self, request, queryset):
        """Turn Authors of selected Comments to an inactive state"""
        for comment in queryset:
            comment.deactivate_comment_author()

    ban_comment_author.short_description = "Deactivate Authors of selected Comments"

    def reactivate_comment_author(self, request, queryset):
        """Turn Authors of selected Comments to an active state"""
        for comment in queryset:
            comment.activate_comment_author()

    reactivate_comment_author.short_description = "Reactivate Authors of selected Comments"


admin.site.register(Comment, AdminComment)


class AdminDenunciaPost(admin.ModelAdmin):
    list_display = ("post", "author", "text", "fecha_creacion")
    list_filter = ("post", "fecha_creacion", "author")
    # Para establecer una jerarquia de fecha
    date_hierarchy = "fecha_creacion"
    actions = ['ban_posts', 'reactivate_posts', 'ban_post_author', 'reactivate_post_author']

    def ban_posts(self, request, queryset):
        """Turn selected Posts to an inactive state"""
        for denuncia in queryset:
            denuncia.post.deactivate_post()

    ban_posts.short_description = "Deactivate selected Posts"

    def reactivate_posts(self, request, queryset):
        """Turn selected Posts to an active state"""
        for denuncia in queryset:
            denuncia.post.activate_post()

    reactivate_posts.short_description = "Reactivate selected Posts"

    def ban_post_author(self, request, queryset):
        """Turn Authors of selected Posts to an inactive state"""
        for denuncia in queryset:
            denuncia.post.deactivate_post_author()

    ban_post_author.short_description = "Deactivate Authors of selected Posts"

    def reactivate_post_author(self, request, queryset):
        """Turn Authors of selected Posts to an active state"""
        for denuncia in queryset:
            denuncia.post.activate_post_author()

    reactivate_post_author.short_description = "Reactivate Authors of selected Posts"


admin.site.register(DenunciaPost, AdminDenunciaPost)


class AdminDenunciaComment(admin.ModelAdmin):
    list_display = ("comment", "author", "text", "fecha_creacion")
    list_filter = ("comment", "fecha_creacion", "author")
    # Para establecer una jerarquia de fecha
    date_hierarchy = "fecha_creacion"
    actions = ['ban_comments', 'reactivate_comments', 'ban_comment_author', 'reactivate_comment_author']

    def ban_comments(self, request, queryset):
        """Turn selected Comments to an inactive state"""
        for denuncia in queryset:
            denuncia.comment.deactivate_comment()

    ban_comments.short_description = "Deactivate selected Comments"

    def reactivate_comments(self, request, queryset):
        """Turn selected Comments to an active state"""
        for denuncia in queryset:
            denuncia.comment.activate_comment()

    reactivate_comments.short_description = "Reactivate selected Comments"

    def ban_comment_author(self, request, queryset):
        """Turn Authors of selected Comments to an inactive state"""
        for denuncia in queryset:
            denuncia.comment.deactivate_comment_author()

    ban_comment_author.short_description = "Deactivate Authors of selected Comments"

    def reactivate_comment_author(self, request, queryset):
        """Turn Authors of selected Comments to an active state"""
        for denuncia in queryset:
            denuncia.comment.activate_comment_author()

    reactivate_comment_author.short_description = "Reactivate Authors of selected Comments"


admin.site.register(DenunciaComment, AdminDenunciaComment)
