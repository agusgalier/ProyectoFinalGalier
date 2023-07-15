from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Futbolista(models.Model):
    nombre=models.CharField(max_length=30)
    edad=models.IntegerField()
    fecha_nacimiento=models.DateField(null=True)
    descripcion=RichTextField(null=True)
    
    def __str__ (self):
            return f'Nombre:{self.nombre}-Edad:{self.edad}'
    
    