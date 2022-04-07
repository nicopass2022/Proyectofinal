from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, Template
from django.template import loader

from AppCoder.forms import cursoformulario

from .models import Articulos, Pedido

def clientes(request):
    return render(request,"appcoder/clientes.html")
    

def inicio(request):
    #return render(request,"appcoder/inicio.html")
    return render(request,"AppCoder/padre.html")
 

# #agregar articulos
def agregaarticulos(request):
    
        codigo=request.POST["codigo"]
        descripcion=request.POST["descripcion"]
        stock=request.POST["stock"]
        articulo=Articulos(Codigo=codigo, descripcion=descripcion,stock=stock)
        articulo.save()
        #return HttpResponse(f"se genero curso {articulo.Codigo} y la camada {articulo.descripcion}")
        return render(request, "AppCoder/productos.html", {"codigo": codigo, "descripcion":descripcion})

    # articulo=Articulos(codigo=codigo,descripcion=descripcion,stock=stock)
    # articulo.save()
    # return HttpResponse(f"se agrego el articulo {articulo.codigo} , {articulo.descipcion}")

def recuperar_articulos(request):
    articulos=Articulos.objects.all()
 
    #contexto= Context({"p":profe})
    return render(request,"AppCoder/recuperar_articulos.html",{"familia":articulos})


def pedidoformulario(request):
    #carga listado de articulos
    articulos=Articulos.objects.all()
    pedidos=Pedido.objects.all()
 
    #contexto= Context({"p":profe})
    #return render(request,"AppCoder/recuperar_articulos.html",{"familia":articulos})

    if request.method=="POST":
        #busco el formulario en forms.py
        miformulario=cursoformulario(request.POST)
        if miformulario.is_valid():
            informacion=miformulario.cleaned_data
            cuit=informacion["cuit"]
            articulo=informacion["articulo"]
            cantidad=informacion["cantidad"]

                
        # curso= Curso , 
        # curso.save()
        # return render (request, "AppCoder/inicio.html")
    return render(request, "AppCoder/pedidoformulario.html",{"pedidos":pedidos})

def agregapedido(request):

        cuit=request.POST["cuit"]
        articulo=request.POST["articulo"]
        cantidad=request.POST["cantidad"]
        descripcion=Pedido(idcliente=cuit, idarticulo=articulo,cantidad=cantidad)
        descripcion.save()
        return HttpResponse(f"se genero pedido")
        #return render(request, "AppCoder/cursos.html", {"codigo": codigo, "descripcion":descripcion})


def productos(request):
    return render(request,"appcoder/productos.html")
    #return HttpResponse("vista de profesores")