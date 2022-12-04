from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class categoria (models.Model):
    nombre = models.CharField(primary_key = True, max_length = 150)
    fecha_creacion = models.DateField(auto_now = True)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"



class autor(models.Model):
    cod = models.AutoField(primary_key = True)
    nombre = models.CharField(null = False, blank = False,max_length = 255)
    apellido = models.CharField(null = False, blank = False,max_length = 255)
    fecha_creacion = models.DateField(auto_now = True)
    def __str__(self):
        return '{} {}'.format(self.nombre,self.apellido)
    
    class Meta:
        verbose_name = "autor"
        verbose_name_plural = "autores"

class libro(models.Model):
    cod = models.AutoField(primary_key = True)
    titulo = models.CharField(null = False, blank = False, max_length = 250)
    descripcion = models.CharField(null = True, blank = True, max_length = 300)
    año_publicacion = models.IntegerField(validators = [MinValueValidator(1700), MaxValueValidator(datetime.date.today().year)])
    autor = models.ForeignKey(autor, on_delete = models.CASCADE)
    categoria = models.ForeignKey(categoria, on_delete = models.CASCADE)
    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = "libro"
        verbose_name_plural = "libros"
    

class publicacion(models.Model):
    cod = models.AutoField(primary_key = True)
    libro = models.ForeignKey(libro, on_delete = models.CASCADE)
    Descripcion = models.CharField(max_length = 300, blank = True)
    fecha_publicacion= models.DateField(auto_now = True,auto_now_add = False)
    imagen_libro = models.ImageField( blank = True, upload_to='media/', default='\media\img_default.png')
    intercambio = models.CharField(max_length = 250, blank = True, null = True)
    creador = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    celular = models.CharField(max_length=10, blank=True)
    
    def __str__(self):
        return  '{} {}'.format(self.cod ,self.libro)
    
    class Meta:
        verbose_name = "publicacion"
        verbose_name_plural = "publicaciones"
    
class perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    libros_favoritos = models.ManyToManyField(libro)
    publicaciones = models.ManyToManyField(publicacion)

