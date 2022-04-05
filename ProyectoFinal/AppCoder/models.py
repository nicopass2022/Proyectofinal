from dataclasses import Field

from django.db import models

# # Create your models here.
# class Curso(models.Model):
#    nombre=models.CharField("nombre", max_length=50)
#    camada = models.IntegerField("camada")

# class Estudiantes(models.Model):
#    nombre=models.CharField("nombre", max_length=50)
#    apellido = models.CharField("apellido", max_length=50)
#    email = models.EmailField()

# class Profesor(models.Model):
#    nombre=models.CharField("nombre", max_length=50)
#    apellido = models.CharField("apellido", max_length=50)
#    email = models.EmailField()
#    profesion= models.CharField("profesion", max_length=50)

# class Entregable(models.Model):
#    nombre=models.CharField("nombre", max_length=50)
#    fecha = models.DateField("fecha", max_length=50)
#    entregado = models.BooleanField()
 
# class Familia(models.Model):
#    nombre=models.CharField("nombre", max_length=50)
#    apellido=models.CharField("apellido", max_length=50)
#    dni = models.IntegerField("dni")
#    fecha_nacimiento=models.CharField("fecha_nacimiento", max_length=50)


#******************************************
class Clientes(models.Model):
   nombre=models.CharField("nombre", max_length=50)
   apellido=models.CharField("apellido", max_length=50)
   razonsocial = models.CharField("razonsocial", max_length=50)
   cuit=models.IntegerField("cuit")
   

class Articulos(models.Model):
   Codigo=models.CharField("codigo", max_length=50)
   descripcion=models.CharField("descripcion", max_length=50)
   stock = models.IntegerField("stock")

class Pedido(models.Model):
   Codigo=models.CharField("codigo", max_length=50)
   idcliente=models.IntegerField("idcliente")
   idarticulo = models.IntegerField("idarticulo")
   cantidad=models.IntegerField("cantidad", default="0")
   entregado=models.BooleanField(default=False)

