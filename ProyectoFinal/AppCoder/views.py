from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, Template
from django.template import loader

from AppCoder.forms import cursoformulario

from .models import Articulos, Pedido
# from .models import Curso, Familia, Profesor
# from AppCoder.models import Profesor

# Create your views here.

# def curso(request,nombre,camada):
#     micurso=Curso(nombre=nombre,camada=camada)
#     micurso.save()
#     #return HttpResponse(f"se genero curso {micurso.nombre} y la camada {micurso.camada}")
#     return render(request, "appcoder/cursos.html", {"nombre": nombre, "camada":camada})

# def profesor(request,nombre,apellido, email,profesion):
#     profe=Profesor(nombre=nombre,apellido=apellido,email=email, profesion=profesion)
#     profe.save()
#     return HttpResponse(f"se agrego el profesor {profe.nombre} , {profe.apellido}")

# def recuperar_profesor(request):
#     profe=Profesor.objects.all()
 
#     #contexto= Context({"p":profe})
#     return render(request,"template2.html",{"profe":profe})


# def recuperar_curso(request):
#     curso=Curso.objects.all()
 
#     #contexto= Context({"p":profe})
#     return render(request,"template_cursos.html",{"curso":curso})
    
# def probandotemplate(request):

#     listaNotas =[1,4,8,10,20] 
#     mihtml= open(r"C:\Users\usuario\Documents\proyecto_coder\ProyectoPrueba\ProyectoPrueba\templates\template1.html")
#     plantilla = Template(mihtml.read())
#     mihtml.close()
#     contexto= Context({"notas":listaNotas})
#     return HttpResponse(plantilla.render(contexto))

def clientes(request):
    return render(request,"appcoder/clientes.html")
    #return HttpResponse("vista de profesores")

# def estudiantes(request):
#     return render(request,"AppCoder/estudiantes.html")

# def entregables(request):
#     return render(request,"appcoder/entregables.html")

def inicio(request):
    #return render(request,"appcoder/inicio.html")
    return render(request,"AppCoder/padre.html")
 
# #agregar familiares
# def agregafamiliar(request,nombre,apellido, dni,fecha_nacimiento):
#     familiar=Familia(nombre=nombre,apellido=apellido,dni=dni,fecha_nacimiento=fecha_nacimiento)
#     familiar.save()
#     return HttpResponse(f"se agrego el familiar {familiar.nombre} , {familiar.apellido}")


# #agregar articulos
def agregaarticulos(request):
    
        codigo=request.POST["codigo"]
        descripcion=request.POST["descripcion"]
        stock=request.POST["stock"]
        articulo=Articulos(Codigo=codigo, descripcion=descripcion,stock=stock)
        articulo.save()
        #return HttpResponse(f"se genero curso {articulo.Codigo} y la camada {articulo.descripcion}")
        return render(request, "AppCoder/cursos.html", {"codigo": codigo, "descripcion":descripcion})

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
