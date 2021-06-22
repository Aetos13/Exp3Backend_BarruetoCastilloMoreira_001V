from django.urls import path
from django.urls.resolvers import URLPattern
from .views import index,galeria,crearObjeto,ver,Modificar,Eliminar

urlpatterns = [
    path ('',index, name="index"), 
    path ('galeria',galeria, name="galeria"),
    path ('index',index, name="index"),
    path('crear_objeto', crearObjeto, name="crearObjeto"),
    path('ver', ver, name="ver"),
    path('modificar/<id>', Modificar, name="modificar"),
    path('eliminar/<id>', Eliminar, name="eliminar")
]