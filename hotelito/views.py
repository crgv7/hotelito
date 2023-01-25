from django.shortcuts import render, redirect
from django.forms import ValidationError
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

def principal(request):
    return render(request,"hotelito/template/principal/index.html")




user=""

class Vregistro(View): # clase regstro, logica que permite registrar al usuario

    def get(self, request):
        form=UserCreationForm()
        return render(request,"hotelito/template/registrar/index.html", {"form":form}) #carga la plantilla y le pasas el formulario
    def post(self, request): # se ejecuta cuando se presiona el boton con la funcion submit haciendo post
        global usuario # se define como global porque se va a usar en otra funcion
        form=UserCreationForm(request.POST)
        if form.is_valid():# comprueba si los datos del formulario son validos
            usuario=form.save()
            login(request, usuario)
            return redirect("/") # redirecciona a la pagina principal
        else: # mensajes de error q muestran que el formulario no es valido
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request,"hotelito/template/registrar/index.html", {"form":form})

def cerrar_sesion(request): # para desloguearse
    logout(request)
    return redirect("/")#redirecciona a la pagina principal



def autenticar (request): # funcion autenticar
    if request.method=="POST":
        print("hizo post")
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_user=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            global usuario
            usuario=authenticate(username=nombre_user, password=contra)
            if usuario is not None: # si usuario no es vacio autentciar
                login(request, usuario)
                return redirect("/")
            else:
                messages.error(request, "usaurio no valido")
        else:
            messages.error(request,"informacion incorrecta")

    form=AuthenticationForm()
    return render(request, "hotelito/template/login/index.html",{"form":form})


