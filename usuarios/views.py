from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView   
from django.contrib.auth import authenticate,login as django_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from usuarios.forms import MiFormularioCreacionUsuarios, MiFormularioEditarPerfil
from django.urls import reverse_lazy
from usuarios.models import InfoExtra

# Create your views here.

def login(request):
    
    if request.method == 'POST':
        formulario=AuthenticationForm(request,data=request.POST)
        if formulario.is_valid():
            usuario=formulario.cleaned_data['username']
            contrasenia=formulario.cleaned_data['password']    
            user=authenticate(username=usuario,password=contrasenia)
            django_login(request,user)
            InfoExtra.objects.get_or_create(user=user)
            return redirect('inicio:inicio')               
        else:
            return render(request,'usuarios/login.html',{'formulario':formulario})
    formulario=AuthenticationForm()
    return render(request,'usuarios/login.html',{'formulario':formulario})

def registrarse(request):
    
    if request.method == 'POST':
        formulario=MiFormularioCreacionUsuarios(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('usuarios:login')
        else:
            return render(request,'usuarios/registrarse.html',{'formulario':formulario})    
    formulario=MiFormularioCreacionUsuarios()
    return render(request,'usuarios/registrarse.html',{'formulario':formulario})    

def mostrar_perfil(request):
    return render(request,'usuarios/mostrar_perfil.html')

@login_required 
def editar_perfil(request):
    info_extra_user=request.user.infoextra 
    if request.method == 'POST':
        formulario=MiFormularioEditarPerfil(request.POST,request.FILES,instance=request.user)
        if formulario.is_valid():
            avatar=formulario.cleaned_data.get('avatar')
            edad=formulario.cleaned_data.get('edad')
            fecha_nacimiento=formulario.cleaned_data.get('fecha_nacimiento')
            descripcion=formulario.cleaned_data.get('descripcion')
            if edad :
                info_extra_user.edad=edad
                info_extra_user.save()
            if fecha_nacimiento:
                info_extra_user.fecha_nacimiento=fecha_nacimiento
                info_extra_user.save()    
            if descripcion:
                info_extra_user.descripcion=descripcion
                info_extra_user.save()    
            if avatar:
                info_extra_user.avatar=avatar
                info_extra_user.save()
            formulario.save()
            return redirect('usuarios:mostrar_perfil')
    else:
        formulario=MiFormularioEditarPerfil(initial={'avatar':info_extra_user.avatar,'edad':info_extra_user.edad,'fecha_nacimiento':info_extra_user.fecha_nacimiento,'descripcion':info_extra_user.descripcion},instance=request.user)     
    return render(request,'usuarios/editar_perfil.html',{'formulario':formulario})

class ModificarPass(LoginRequiredMixin,PasswordChangeView):
    template_name='usuarios/modificar_pass.html'
    success_url=reverse_lazy('usuarios:editar_perfil')