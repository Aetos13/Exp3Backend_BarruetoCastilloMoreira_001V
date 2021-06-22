from django.shortcuts import render, redirect
from .models import Objeto
from .forms import ObjetoForm


def index(request):
    return render(request, 'index.html')

    
def galeria(request):
    return render(request, 'Galeria.html')


def crearObjeto(request):
    if request.method=='POST': 
        objeto_form = ObjetoForm(request.POST)
        if objeto_form.is_valid():
            objeto_form.save()
            return redirect('ver')
    else:
        objeto_form= ObjetoForm()
    return render(request, 'core/form_crearobjeto.html', {'objeto_form': objeto_form})


def ver(request):
    objetos = Objeto.objects.all()

    return render(request, 'core/ver.html', context={'objetos':objetos})


def Modificar(request,id):
    objeto = Objeto.objects.get(id=id)

    datos ={
        'form': ObjetoForm(instance=objeto)
    }
    if request.method == 'POST': 
        formulario = ObjetoForm(data=request.POST, instance = objeto)
        if formulario.is_valid: 
            formulario.save()           
            return redirect('ver')
    return render(request, 'core/form_mod_objeto.html', datos)


def Eliminar(request,id):
    objeto = Objeto.objects.get(id=id)
    objeto.delete()
    return redirect('ver')