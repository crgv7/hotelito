from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Disponibilidad(models.Model):
    habitaciones=models.IntegerField(blank=False, null=True)
    fecha=models.DateTimeField(blank=False, null=False)    
    user=models.ForeignKey(User, on_delete=models.CASCADE) 
    
    def __str__(self):
        return ' Disponibilidad para '+ self.user.username
        
    # end def