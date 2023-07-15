from django.urls import path
from inicio import views

app_name='inicio'

urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('futbolistas/crear/',views.CrearFutbolista.as_view(),name='crear_futbolista'),
    path('futbolistas/',views.ListaFutbolistas.as_view(),name='futbolistas'),
    path('futbolistas/<int:pk>/',views.InformacionFutbolista.as_view(),name='informacion_futbolista'),
    path('futbolistas/<int:pk>/modificar/',views.ModificarFutbolista.as_view(),name='modificar_futbolista'),
    path('futbolistas/<int:pk>/eliminar/',views.EliminarFutbolista.as_view(),name='eliminar_futbolista'),  
             
]
