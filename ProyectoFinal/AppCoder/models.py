from dataclasses import Field

from django.db import models

class Articulos(models.Model):
   Codigo=models.CharField("codigo", max_length=50)
   descripcion=models.CharField("descripcion", max_length=50)
   stock = models.IntegerField("stock")


class Clientes(models.Model):
   nombre=models.CharField("nombre", max_length=50)
   apellido=models.CharField("apellido", max_length=50)
   razonsocial = models.CharField("razonsocial", max_length=50)
   cuit=models.IntegerField("cuit")
   

class Pedido(models.Model):
   idcliente=models.IntegerField("idcliente")
   idarticulo = models.IntegerField("idarticulo")
   cantidad=models.IntegerField("cantidad", default="0")
   entregado=models.BooleanField(default=False)

