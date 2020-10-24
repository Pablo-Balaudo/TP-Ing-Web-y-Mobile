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

    def deactivate_post(self):
        """Set Post Active state to False"""
        self.active = False
        self.save()

    def activate_post(self):
        """Set Post Active state to True"""
        self.active = True
        self.save()

    def deactivate_post_author(self):
        """Set Post Author state to False"""
        self.author.is_active = False
        self.author.save()

    def activate_post_author(self):
        """Set Post Author state to True"""
        self.author.is_active = True
        self.author.save()


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

    def deactivate_comment(self):
        """Set Comment Active state to False"""
        self.active = False
        self.save()

    def activate_comment(self):
        """Set Comment Active state to True"""
        self.active = True
        self.save()

    def deactivate_comment_author(self):
        """Set Comment Author state to False"""
        self.author.is_active = False
        self.author.save()

    def activate_comment_author(self):
        """Set Comment Author state to True"""
        self.author.is_active = True
        self.author.save()


class DenunciaPost(Denuncia):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.post.pk})


class DenunciaComment(Denuncia):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.post.pk})
