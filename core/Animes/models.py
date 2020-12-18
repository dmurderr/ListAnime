from django.db import models
from django.apps import AppConfig
# Create your models here.



class Genero(models.Model):
    generosId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50 , unique = True)


    class Meta:
        verbose_name = ("Genero")
        verbose_name_plural = ("Generos")

    def __str__(self):
        return self.name

class Author(models.Model):

    name = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50) 


    class Meta:
        verbose_name = ("Autor")
        verbose_name_plural = ("Autores")
        ordering = ['id']

    def __str__(self):
        self.nombreCompleto = '{} {}'.format(self.name , self.apellido)
        return self.nombreCompleto
        


class Anime(models.Model):
    
    animeid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50 , unique = True)
    date = models.DateField(auto_now=False, auto_now_add=False)
    autor = models.ManyToManyField(Author,  symmetrical = False )
    genero = models.ManyToManyField(Genero, verbose_name=("Genero") , symmetrical = False)
    imagen = models.ImageField(upload_to="media", height_field=None, width_field=None, max_length=None)
    
    
    class Meta:
        verbose_name = ("Anime")
        verbose_name_plural = ("Animes")

    def __str__(self):
        return self.name

    def ruta(self):
        self.ruta = self.imagen
        return self.ruta