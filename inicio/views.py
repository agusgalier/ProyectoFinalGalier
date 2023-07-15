from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from inicio.forms import CrearFutbolistaFormulario, BusquedaFutbolistaFormulario
from inicio.models import Futbolista
from django.views.generic.edit import UpdateView,DeleteView, CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy    
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def inicio(request):
    return render(request,'inicio/inicio.html')

class CrearFutbolista(CreateView):
    model=Futbolista
    template_name='inicio/crear_futbolista.html'
    fields=['nombre','edad','fecha_nacimiento','descripcion']
    success_url=reverse_lazy('inicio:futbolistas')

class ListaFutbolistas(ListView):
    model= Futbolista
    template_name = "inicio/futbolistas.html"
    context_object_name='futbolistas'
    
    def get_queryset(self):
        lista_de_futbolistas=[]
        formulario=BusquedaFutbolistaFormulario(self.request.GET)  
        if formulario.is_valid():
            nombre_a_buscar=formulario.cleaned_data['nombre']
            lista_de_futbolistas=Futbolista.objects.filter(nombre__icontains=nombre_a_buscar)    
        return lista_de_futbolistas
    
    def get_context_data(self, **kwargs):
       contexto=super().get_context_data(**kwargs)
       contexto['formulario']=BusquedaFutbolistaFormulario()
       return contexto
   
class InformacionFutbolista(DetailView):
    model = Futbolista
    template_name = "inicio/informacion_futbolista.html"

class ModificarFutbolista(LoginRequiredMixin,UpdateView):
    model = Futbolista
    fields= ['nombre','edad','fecha_nacimiento','descripcion']
    template_name = "inicio/modificar_futbolista.html"
    success_url=reverse_lazy('inicio:futbolistas')
    
class EliminarFutbolista(LoginRequiredMixin,DeleteView):
    model = Futbolista
    template_name = "inicio/eliminar_futbolista.html"
    success_url=reverse_lazy('inicio:futbolistas')
    