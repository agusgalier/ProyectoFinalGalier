from django.shortcuts import render
from inicio.forms import CrearFutbolistaFormulario
from inicio.models import Futbolista


# Create your views here.

def inicio(request):
    return render(request,'inicio/inicio.html')

def crear_futbolista(request):
    mensaje=''
    
    if request.method=='POST':
        formulario=CrearFutbolistaFormulario(request.POST)
        if formulario.is_valid():
            info=formulario.cleaned_data
            futbolista=Futbolista(nombre=info['nombre'],edad=info['edad'],fecha_nacimiento=info['fecha_nacimiento'])  
            futbolista.save()
            mensaje=f'Se creo el futbolista {futbolista.nombre}'        
        else:
            return render(request,'inicio/crear_futbolista.html',{'formulario':formulario})        
    
    formulario=CrearFutbolistaFormulario()
    return render(request,'inicio/crear_futbolista.html',{'formulario':formulario,'mensaje':mensaje})