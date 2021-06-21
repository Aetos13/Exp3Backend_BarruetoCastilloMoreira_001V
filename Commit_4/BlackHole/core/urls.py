from django.urls import path
from django.urls.resolvers import URLPattern
from .views import index,galeria

urlpatterns = [
    path ('',index, name="index"), 
    #path ('',galeria, name="galeria"),
]