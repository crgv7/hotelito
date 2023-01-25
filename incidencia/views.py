from django.shortcuts import render
from django.shortcuts import render,redirect
from incidencia.models import Incidencia   #importa el modelo del models.py
from incidencia.forms import incidenciaform # importa el formulario  del archivo form
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.

@login_required
def panel(request):

    incidencia=Incidencia.objects.all().filter(user=request.user) # para hacer filtro hace una consulta select y lo filtra por el nombre de usuario
    
    buscar=request.POST.get('buscar')
    
  
    if buscar:
        incidencia=Incidencia.objects.filter(
         Q(nombre__icontains = buscar)| 
         Q(incidencia__icontains = buscar) 
        ).distinct()
   
    return render(request, "incidencia/template/panel_incidencia.html", {"incidencia": incidencia}) # carga el html
                                                                                                                        # y sele pasa
                                                                                                                        #los objetos de la                                                                                                                        # base de datos a la
@login_required                                                                                                                        # plantilla html
def add_incidencia(request):
        context={}
     
        if request.method == "POST": # si el metod es post realiza la condicion
            form=incidenciaform(request.POST)     
            form.user=request.user
            if form.is_valid():                                  # validacion del formula
                nombre=form.cleaned_data.get("nombre")
                incidencia=form.cleaned_data.get("incidencia")
                fecha=form.cleaned_data.get("fecha")

                reg=Incidencia.objects.create( #crea objetos en la tabla
                    nombre=nombre,
                    incidencia=incidencia,                  
                    fecha=fecha,
                   user=request.user
                )
                reg.save()


# si no es post muestra el formulario

        form=incidenciaform()                                                             
    
        context["form"]=form
        return render(request, "incidencia/template/add_incidencia.html", context)
@login_required
def eliminar(request, id): # eliminar obejeto
    incidencia=Incidencia.objects.all().filter(user=request.user)
    incident=Incidencia.objects.get(id=id)
    incident.delete()
    return redirect("/paneli/")
@login_required
def editar(request, id): # editar reservacion

    incident=Incidencia.objects.get(id=id)

    context={}
    form=incidenciaform(initial={'nombre': incident.nombre,
                                  'incidencia': incident.incidencia,                       
                                  'fecha': incident.fecha,
    })
                                  
    context["form"]=form

    if request.method == "POST":
        form=incidenciaform(request.POST)

        if form.is_valid():                                  # validacion del formula
            nombre=form.cleaned_data.get("nombre")
            incidencia=form.cleaned_data.get("incidencia")         
            fecha=form.cleaned_data.get("fecha")
            

            incident.nombre=nombre
            incident.incidencia=incidencia
            incident.fecha=fecha

            incident.save()
            return redirect('/paneli/')

    return render(request, "incidencia/template/editar_incidencia.html", context)
