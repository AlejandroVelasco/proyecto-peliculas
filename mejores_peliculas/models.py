from django.db import models

# Create your models here.
class Director(models.Model):    
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)

    def nombre_completo(self):
        return f"{self.nombres} {self.apellidos}"

    def __str__(self):
        return self.nombre_completo()


class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    # director = models.CharField(max_length=100)
    anio = models.IntegerField()
    genero = models.CharField(max_length=100)
    duracion = models.IntegerField()
    quote = models.CharField(max_length=200)
    imagen = models.CharField(max_length=200)
    sinopsis = models.TextField()
    votos = models.IntegerField()
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True, related_name="post_director_fk")


class Comentario(models.Model):    
    nombre = models.CharField(max_length=100)    
    correo = models.EmailField()
    comentario = models.TextField()
    post = models.ForeignKey(Pelicula, on_delete= models.CASCADE, related_name="fg_comentario_post")
