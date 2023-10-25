from django.db import models

# Create your models here.
class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    anio = models.IntegerField
    genero = models.CharField(max_length=100)
    duracion = models.IntegerField()
    quote = models.CharField(max_length=200)
    imagen = models.CharField(max_length=200)
    sinopsis = models.CharField(max_length=2000)
    votos = models.IntegerField()
