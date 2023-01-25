from django import forms
from .models import Reservacion






#formulario

class reservacionform(forms.ModelForm):
    cantidad_habitaciones=forms.IntegerField(initial=1,max_value=5,min_value=1,disabled=False)

    class Meta:
        model=Reservacion
        fields=[
            "nombre",
            "apellido",
            "ci",
            "telefono",
            "fecha",
            "cantidad_habitaciones",

        ]
        widgets={
            "nombre": forms.TextInput(attrs={"class": "form-input", "id":"nombre", "Placeholder":"nombre"}),
            "apellido": forms.TextInput(attrs={"class": "form-input","Placeholder": "apellido", "id":"apellido"}),
            "telefono": forms.TextInput(attrs={"class": "form-input","Placeholder": "telefono", "id":"telefono"}),
            "fecha": forms.TextInput(attrs={"class": "form-input","Placeholder": "dia/mes", "id":"fecha"}),
            "ci": forms.TextInput(attrs={"class": "form-input","Placeholder": "CI", "id":"ci"}),

        }
