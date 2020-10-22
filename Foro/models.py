from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from Usuarios.models import Denuncia


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.author)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.post.pk})

    def get_post_number(self):
        return self.post


class DenunciaPost(Denuncia):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class DenunciaComment(Denuncia):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
