from django.db import models
from datetime import datetime

# Create your models here.

class Curso(models.Model):

    curso_titulo= models.CharField(max_length=200)
    curso_contenido= models.TextField()
    curso_publicado= models.DateTimeField("fecha de publicacion", default=datetime.now())
    costo = models.DecimalField(max_digits=5, decimal_places=2, default=0)


    def __str__(self):
        return self.curso_titulo
