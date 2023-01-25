from django.shortcuts import render
from django.shortcuts import render,redirect
from reservacion.models import Reservacion   #importa el modelo del models.py
from reservacion.forms import reservacionform # importa el formulario  del archivo form
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.

@login_required
def panel(request):
    
    reservaciones=Reservacion.objects.all().filter(user=request.user) # para hacer filtro hace una consulta select y lo filtra por el nombre de usuario
    buscar=request.POST.get('buscar')
    
  
    if buscar:
        reservaciones=Reservacion.objects.filter(
         Q(nombre__icontains = buscar)| 
         Q(apellido__icontains = buscar) 
        ).distinct()

   
    return render(request, "reservacion/template/panel_reservacion/panel.html", {"reservaciones":reservaciones}) # carga el html
                                                                                                                        # y sele pasa
                                                                                                                        #los objetos de la                                                                                                                        # base de datos a la
@login_required                                                                                                                        # plantilla html
def add_reservacion(request):
        context={}
     
        if request.method == "POST": # si el metod es post realiza la condicion
            form=reservacionform(request.POST)     
            form.user=request.user
            if form.is_valid():                                  # validacion del formula
                nombre=form.cleaned_data.get("nombre")
                apellido=form.cleaned_data.get("apellido")
                telefono=form.cleaned_data.get("telefono")
                fecha=form.cleaned_data.get("fecha")
                ci=form.cleaned_data.get("ci")
                cantidad_habitaciones=form.cleaned_data.get("cantidad_habitaciones")

                reg=Reservacion.objects.create( #crea objetos en la tabla
                    nombre=nombre,
                    apellido=apellido,
                    telefono=telefono,
                    fecha=fecha,
                    ci=ci,
                   cantidad_habitaciones=cantidad_habitaciones,
                   user=request.user
                )
                reg.save()


# si no es post muestra el formulario

        form=reservacionform()                                                             
    
        context["form"]=form
        return render(request, "reservacion/template/panel_reservacion/add_reservacion.html", context)
@login_required
def eliminar(request, id): # eliminar obejeto
    reservaciones=Reservacion.objects.all().filter(user=request.user)
    reserv=Reservacion.objects.get(id=id)
    reserv.delete()
    return redirect("/panel/")
@login_required
def editar(request, id): # editar reservacion

    reserv=Reservacion.objects.get(id=id)

    context={}
    form=reservacionform(initial={'nombre': reserv.nombre,
                                  'apellido': reserv.apellido,
                                  'telefono': reserv.telefono,
                                  'ci': reserv.ci,
                                  'fecha': reserv.fecha,
                                  'cantidad_habitaciones': reserv.cantidad_habitaciones})
    context["form"]=form

    if request.method == "POST":
        form=reservacionform(request.POST)

        if form.is_valid():                                  # validacion del formula
            nombre=form.cleaned_data.get("nombre")
            apellido=form.cleaned_data.get("apellido")
            telefono=form.cleaned_data.get("telefono")
            ci=form.cleaned_data.get("ci")
            fecha=form.cleaned_data.get("fecha")
            cantidad_habitaciones=form.cleaned_data.get("cantidad_habitaciones")

            reserv.nombre=nombre
            reserv.apellido=apellido
            reserv.telefono=telefono
            reserv.ci=ci
            reserv.fecha=fecha
            reserv.cantidad_habitaciones=cantidad_habitaciones

            reserv.save()
            return redirect('/panel/')

    return render(request, "reservacion/template/panel_reservacion/editar_reservacion.html", context)
