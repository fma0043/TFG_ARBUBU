from django.shortcuts import render

from django.views.generic import(
    TemplateView,
    ListView,
)
# Create your views here.
class IndexView(TemplateView):

    template_name = "home/index.html"

class ListaArbol(ListView):

    template_name = "home/lista.html"
    queryset = ['nogal','manzano','naranjo','peral']
    context_object_name = 'arboles'
