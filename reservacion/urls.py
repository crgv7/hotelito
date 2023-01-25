
from django.urls import path
from reservacion.views import panel,add_reservacion,eliminar,editar



urlpatterns = [
    path("panel/add_reservacion/", add_reservacion),
    path("", panel),
    path("panel/eliminar/<id>", eliminar),
    path("panel/editar/<id>", editar),
]
