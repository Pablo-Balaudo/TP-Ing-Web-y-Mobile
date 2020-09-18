from django.db import models
from django.contrib.auth.models import User

class Base(models.Model):
    idComentario = models.AutoField(primary_key=True)
    fechainicio = models.DateTimeField(auto_now_add = True)
