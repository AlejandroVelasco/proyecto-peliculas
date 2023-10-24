from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="pagina-inicial"),
    path("ranking", views.index, name="pagina-ranking"),
    path("<int:id>", views.detalle, name="pagina-detalle"),
]
