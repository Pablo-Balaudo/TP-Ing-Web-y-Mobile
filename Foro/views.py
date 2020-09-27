from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


# class PostListView(ListView):


def foro(request):
    contenido = {'Posts': Post.objects.all()}
    return render(request, 'Foro/Foro.html', contenido)
