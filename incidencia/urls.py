
from django.urls import path
from incidencia.views import *



urlpatterns = [
    path("paneli/add_incidencia/", add_incidencia),
    path("", panel),
    path("paneli/eliminar/<id>", eliminar),
    path("paneli/editar/<id>", editar),
]