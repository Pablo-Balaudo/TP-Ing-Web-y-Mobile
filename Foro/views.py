from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin)
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView, )
from .models import *
from .forms import CommentForm


def foro(request):
    contenido = {'Posts': Post.objects.all()}
    return render(request, 'Foro/Foro.html', contenido)


class PostListView(ListView):
    model = Post  # Use the Post model
    template_name = 'Foro/Foro.html'  # Use this view instead of the default one
    context_object_name = 'Posts'  # Be referred to as "Post", as indicated in "contenido"
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(active=True).order_by('-date_posted')


class UserPostListView(ListView):
    model = Post  # Use the Post model
    template_name = 'Foro/user_post.html'  # Use this view instead of the default one
    context_object_name = 'Posts'  # Be referred to as "Post", as indicated in "contenido"
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user, active=True).order_by('-date_posted')


def post_detail(request, pk):
    template_name = 'Foro/post_detail.html'
    post = get_object_or_404(Post, pk=pk)
    author = get_object_or_404(User, id=request.user.id)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            new_comment.author = author
            # Save the comment to the database
            new_comment.save()
        return redirect('post-detail', pk=post.pk)
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post  # Use the Post model
    fields = ['title', 'text']

    def form_valid(self, form):  # Check to stop non logged users from posting
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post  # Use the Post model
    fields = ['title', 'text']

    def form_valid(self, form):  # Check to stop non logged users from posting
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


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment  # Use the Comment model
    fields = ['text', ]

    def form_valid(self, form):  # Check to stop non logged users from commenting
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):  # Check to stop non authors from updating
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment  # Use the Comment model

    def get_success_url(self):
        return f'/foro/post/{self.get_object().post.id}'

    def test_func(self):  # Check to stop non authors from updating
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
