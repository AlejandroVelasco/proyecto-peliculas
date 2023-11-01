from django.contrib import admin
from .models import Pelicula, Director, Comentario

# Register your models here.
class PeliculaAdmin(admin.ModelAdmin):
    list_filter=("titulo","director", "anio")    
    list_display = ("titulo","director")    

class ComentarioAdmin(admin.ModelAdmin):    
    list_display = ("nombre","correo","comentario")    
    
admin.site.register(Pelicula, PeliculaAdmin)
admin.site.register(Director)
admin.site.register(Comentario, ComentarioAdmin)