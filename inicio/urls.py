from django.urls import path
from inicio import views

app_name='inicio'

urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('futbolistas/crear/',views.crear_futbolista,name='crear_futbolista'),
]
