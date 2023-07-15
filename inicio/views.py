from django.shortcuts import render
from inicio.forms import CrearFutbolistaFormulario, BusquedaFutbolistaFormulario
from inicio.models import Futbolista
from django.views.generic.edit import UpdateView,DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

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

def listar_futbolistas(request):
    
    
    formulario=BusquedaFutbolistaFormulario(request.GET)
    if formulario.is_valid():
        nombre_a_buscar=formulario.cleaned_data.get('nombre', '')
        lista_futbolistas=Futbolista.objects.filter(nombre__icontains=nombre_a_buscar)
    
    formulario=BusquedaFutbolistaFormulario()
    return render(request,'inicio/futbolistas.html',{'formulario':formulario,'lista_futbolistas':lista_futbolistas})

class InformacionFutbolista(DetailView):
    model = Futbolista
    template_name = "inicio/informacion_futbolista.html"

class ModificarFutbolista(UpdateView):
    model = Futbolista
    fields= ['nombre','edad','fecha_nacimiento']
    template_name = "inicio/modificar_futbolista.html"
    success_url=reverse_lazy('inicio:futbolistas')
    
class EliminarFutbolista(DeleteView):
    model = Futbolista
    template_name = "inicio/eliminar_futbolista.html"
    success_url=reverse_lazy('inicio:futbolistas')
    