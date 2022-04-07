from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, Template
from django.template import loader

#from AppCoder.forms import cursoformulario

from .models import Articulos, Clientes, Pedido

def clientes(request):
            clientes=Clientes.objects.all()
 
            #contexto= Context({"p":profe})
            return render(request,"AppCoder/clientes.html",{"clientes":clientes})



    #return render(request,"AppCoder/clientes.html")
    


def agregaclientes(request):
    
        nombre=request.POST["nombre"]
        apellido=request.POST["apellido"]
        razonsocial=request.POST["razonsocial"]
        cuit=request.POST["cuit"]
        cliente=Clientes(nombre=nombre, apellido=apellido, razonsocial=razonsocial, cuit=cuit)
        cliente.save()
        #return HttpResponse(f"se genero curso {articulo.Codigo} y la camada {articulo.descripcion}")
        
        clientes=Clientes.objects.all()
 
        #contexto= Context({"productos":articulos} )

        return render(request,"AppCoder/clientes.html",{"clientes":clientes, "razonsocial": razonsocial, "cuit": cuit})



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
        
        articulos=Articulos.objects.all()
 
        #contexto= Context({"productos":articulos} )

        return render(request,"AppCoder/productos.html",{"productos":articulos, "descripcion": descripcion, "codigo": codigo})
        
        #return render(request, "AppCoder/productos.html", {"codigo": codigo, "descripcion":descripcion})

    # articulo=Articulos(Codigo=codigo,descripcion=descripcion,stock=stock)
    # articulo.save()
    # return HttpResponse(f"se agrego el articulo {articulo.codigo} , {articulo.descipcion}")

def recuperar_articulos(request):
    articulos=Articulos.objects.all()
 
    #contexto= Context({"p":profe})
    return render(request,"AppCoder/recuperar_articulos.html",{"familia":articulos})


def pedidos(request):
    #carga listado de articulos
    # articulos=Articulos.objects.all()
    # pedidos=Pedido.objects.all()
 
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
    pedidos=Pedido.objects.all()
    return render(request, "AppCoder/pedidos.html",{"pedidos":pedidos})

def agregapedido(request):

        cuit=request.POST["cuit"]
        articulo=request.POST["articulo"]
        cantidad=request.POST["cantidad"]
        descripcion=Pedido(idcliente=cuit, idarticulo=articulo,cantidad=cantidad)
        descripcion.save()

        pedidos=Pedido.objects.all()
        productos=Articulos.objects.all()
        return render(request, "AppCoder/pedidos.html",{"pedidos":pedidos, "productos":productos, "descripcion":descripcion, "articulo":articulo, })
        #return HttpResponse(f"se genero pedido")
        #return render(request, "AppCoder/cursos.html", {"codigo": codigo, "descripcion":descripcion})


def productos(request):

            articulos=Articulos.objects.all()
 
            #contexto= Context({"p":profe})
            return render(request,"AppCoder/productos.html",{"productos":articulos})
    #return render(request,"appcoder/productos.html")
    #return HttpResponse("vista de profesores")