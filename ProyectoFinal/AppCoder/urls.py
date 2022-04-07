
from django.urls import path

from .views import agregaarticulos, agregapedido, clientes, inicio,  pedidoformulario, recuperar_articulos, productos
# from .views import curso, cursoformulario, estudiantes, entregables, inicio, profesores

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('inicio/', inicio, name="Inicio"),
    # path('agrega-curso/<nombre>/<camada>', curso),
    path('clientes/', clientes, name="clientes"),
    path('recuperar_articulos/', recuperar_articulos, name="recuperar_articulos"),
    path('agregaarticulos/', agregaarticulos, name="agregaarticulos"),
    path('agregapedido/', agregapedido, name="agregapedido"),
    # path('entregables/', entregables, name="Entregables"),
    path('pedidormulario/', pedidoformulario, name="pedidoformulario"),
    path('productos/', productos, name="productos")
    
    
]

