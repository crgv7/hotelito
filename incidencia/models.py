from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Incidencia(models.Model):
    nombre=models.CharField(max_length=15)
    incidencia=models.CharField(max_length=200) 
    fecha=models.CharField(max_length=10)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    