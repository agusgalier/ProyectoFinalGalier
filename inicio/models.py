from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Futbolista(models.Model):
    nombre=models.CharField(max_length=30)
    posicion=models.CharField(max_length=20,null=True)
    edad=models.IntegerField()
    fecha_nacimiento=models.DateField(null=True)
    descripcion=RichTextField(null=True)
    autor=models.CharField(max_length=30,null=True)
    
    def __str__ (self):
            return f'Nombre:{self.nombre}-Edad:{self.edad}'
    
    