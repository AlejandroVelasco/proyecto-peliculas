from django import forms
from .models import Comentario

class FormComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        exclude = ["post"] # Del modelo Comentario excluimos el atributo post porque este no debe aparecer en el form
        labels = { 
            "nombre":"Escribe tu nombre",
            "correo":"Digite su correo acá",
            "comentario":"Escribe tu comentario: ",
        }

