from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Reservacion(models.Model):
    nombre=models.CharField(max_length=15)
    apellido=models.CharField(max_length=15)
    ci=models.IntegerField()
    telefono=models.IntegerField()
    fecha=models.CharField(max_length=10)
    cantidad_habitaciones=models.IntegerField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)