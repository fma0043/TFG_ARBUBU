from django.shortcuts import render

from django.views.generic import(
    TemplateView,
    ListView,
    CreateView,
)

from .models import Familia,Especie,Individuos
# Create your views here.

class ListaArboles(ListView):

    template_name = "pantallaPrincipal/lista-familias.html"
    model = Familia
    context_object_name = 'familia'

class ListaEspecies(ListView):

    template_name = "pantallaPrincipal/lista-especies.html"
    #model = Especie
    context_object_name = 'especie'

    def get_queryset(self):
        id = self.kwargs['pk']
        lista = Especie.objects.filter(
            familia=id
        )
        # devuelvo el resultado o la lista resultado
        return lista

class ListaIndividuos(ListView):

    template_name = "pantallaPrincipal/lista-individuos.html"
    context_object_name = 'individuo'

    def get_queryset(self):
        id = self.kwargs['pk']
        lista = Individuos.objects.filter(
            especie=id
        )
        # devuelvo el resultado o la lista resultado
        return lista

class AddIndividuo(CreateView):
    """ vista para registrar un nuevo Individuo """
    template_name = 'pantallaPrincipal/add-individuo.html'
    model = Individuos
    fields = ['nombreIndividuos', 'caracteristicas','especie']
    success_url = '/'

#href="{% url 'pantallaPrincipal_app:lista-individuos' l.id %}"
