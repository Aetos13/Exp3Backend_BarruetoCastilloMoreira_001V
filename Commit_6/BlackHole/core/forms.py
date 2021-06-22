from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Categoria, Objeto

class ObjetoForm(forms.ModelForm):

    class Meta: 
        model= Objeto
        fields = ['id', 'marca', 'articulo', 'categoria']
        labels ={
            'patente': 'Patente', 
            'marca': 'Marca', 
            'modelo': 'Modelo', 
            'categoria': 'Categoría',
        }
        widgets={
            'id': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese id', 
                    'id': 'id'
                }
            ), 
            'marca': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese marca', 
                    'id': 'marca'
                }
            ), 
            'articulo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese articulo', 
                    'id': 'articulo'
                }
            ), 
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'categoria',
                }
            )

        }