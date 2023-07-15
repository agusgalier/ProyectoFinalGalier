from django import forms

class CrearFutbolistaFormulario(forms.Form):
   nombre=forms.CharField( max_length=30)
   edad=forms.IntegerField()
   fecha_nacimiento=forms.DateField(required=False, widget=forms.DateInput(format='%d/%m/%Y'),input_formats=('%d/%m/%Y',))
   
class BusquedaFutbolistaFormulario(forms.Form):
   nombre=forms.CharField(max_length=30,required=False)     