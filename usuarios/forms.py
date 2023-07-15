from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class MiFormularioCreacionUsuarios(UserCreationForm):
    email=forms.EmailField()
    password1=forms.CharField(label='Contrasenia',widget=forms.PasswordInput)
    password2=forms.CharField(label='Repetir Contrasenia',widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields=['username','email','password1','password2']        
        help_texts={k:"" for k in fields}

class MiFormularioEditarPerfil(UserChangeForm):
    password=None
    email= forms.EmailField()
    first_name=forms.CharField(label='Nombrre',max_length=20)
    last_name=forms.CharField(label='Apellido',max_length=20)
    avatar=forms.ImageField(required=False)
    
    class Meta:
        model=User
        fields=['email','first_name','last_name','avatar']