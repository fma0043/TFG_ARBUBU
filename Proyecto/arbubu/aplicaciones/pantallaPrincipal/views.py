from django.shortcuts import render

from django.views.generic import(
    TemplateView,
    ListView,
)

from .models import Familia,Especie,Individuos
# Create your views here.

class ListaArboles(ListView):

    template_name = "pantallaPrincipal/lista-arboles.html"
    model = Familia
    context_object_name = 'arbol'
