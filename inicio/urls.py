from django.urls import path
from inicio import views

app_name='inicio'

urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('futbolistas/crear/',views.crear_futbolista,name='crear_futbolista'),
    path('futbolistas/',views.listar_futbolistas,name='futbolistas'),
    path('futbolistas/<int:pk>/',views.InformacionFutbolista.as_view(),name='informacion_futbolista'),
    path('futbolistas/<int:pk>/modificar/',views.ModificarFutbolista.as_view(),name='modificar_futbolista'),
    path('futbolistas/<int:pk>/eliminar/',views.EliminarFutbolista.as_view(),name='eliminar_futbolista'),  
             
]
