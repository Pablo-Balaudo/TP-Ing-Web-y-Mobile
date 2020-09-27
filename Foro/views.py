from django.shortcuts import render
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post


def foro(request):
    contenido = {'Posts': Post.objects.all()}
    return render(request, 'Foro/Foro.html', contenido)


class PostListView(ListView):
    model = Post  # Use the Post model
    template_name = 'Foro/Foro.html'  # Use this view instead of the default one
    context_object_name = 'Posts'  # Be referred to as "Post", as indicated in "contenido"
    ordering = ['-date_posted']  # Show newer posts first


class PostDetailedView(DetailView):
    model = Post  # Use the Post model


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post  # Use the Post model
    fields = ['title', 'text']

    def form_valid(self, form):  # Check to stop non logged users from post
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post  # Use the Post model
    fields = ['title', 'text']

    def form_valid(self, form):  # Check to stop non logged users from post
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):  # Check to stop non authors from updating
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post  # Use the Post model
    success_url = '/foro'

    def test_func(self):  # Check to stop non authors from updating
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
