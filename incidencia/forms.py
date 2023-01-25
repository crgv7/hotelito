from django import forms
from .models import Incidencia

#formulario

class incidenciaform(forms.ModelForm):
    

    class Meta:
        model=Incidencia
        fields=[
            "nombre",
            "incidencia",
            "fecha",
      
        ]
        widgets={
            "nombre": forms.TextInput(attrs={"class": "form-input", "id":"nombre", "Placeholder":"nombre"}),
            "incidencia": forms.Textarea(attrs={"class": "form-input","Placeholder": "incidencia", "id":"incidencia"}),
            "fecha": forms.TextInput(attrs={"class": "form-input","Placeholder": "fecha", "id":"fecha"}),
          
        }
