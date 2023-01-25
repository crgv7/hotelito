from django.contrib import admin
from .models import Disponibilidad

# Register your models here.

class Disponibilidadadmin(admin.ModelAdmin):
    list_display=("user","fecha","habitaciones")


admin.site.register(Disponibilidad, Disponibilidadadmin)
