from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de Categoria')
    nombreCategoria = models.CharField(max_length=50,verbose_name='Nombre Categoria')

    def __str__(self):
        return self.nombreCategoria

class Objeto(models.Model):
    id = models.CharField(max_length=6, primary_key=True, verbose_name='Id')
    marca = models.CharField(max_length=20, verbose_name='Marca del Vehiculo')
    articulo = models.CharField(max_length=20, verbose_name='Articulo')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.id