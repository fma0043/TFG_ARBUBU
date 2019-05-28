from django.shortcuts import render

from django.template import RequestContext

from django.views.generic import(
    ListView,
    TemplateView,
    CreateView,
)

from .models import Familia,Especie,Individuos,Usuario
# Create your views here.

class IndexView(TemplateView):

    template_name = "pantallaPrincipal/index.html"

class ListaFamilias(ListView):

    template_name = "pantallaPrincipal/lista-familias.html"
    model = Familia
    context_object_name = 'familia'


class ListaEspecies(ListView):

    template_name = "pantallaPrincipal/lista-especies.html"
    model = Especie
    context_object_name = 'especie'

    #def get_queryset(self):
    #    id = self.kwargs['pk']
    #    lista = Especie.objects.filter(
    #        familia=id
    #    )
        # devuelvo el resultado o la lista resultado
    #    return lista

class ListaIndividuos(ListView):

    template_name = "pantallaPrincipal/lista-individuo.html"
    model = Individuos
    context_object_name = 'individuo'

class ListaUsuarios(ListView):

    template_name = "pantallaPrincipal/lista-usuario.html"
    model = Usuario
    context_object_name = 'usuario'

    #def get_queryset(self):
    #    id = self.kwargs['pk']
    #    lista = Individuos.objects.filter(
    #        especie=id
    #    )
        # devuelvo el resultado o la lista resultado
    #    return lista

#class AddIndividuo(CreateView):
#    """ vista para registrar un nuevo Individuo """
#    template_name = 'pantallaPrincipal/add-individuo.html'
#    model = Individuos
#    fields = ['nombreIndividuos', 'caracteristicas','especie']
#    success_url = '/'
