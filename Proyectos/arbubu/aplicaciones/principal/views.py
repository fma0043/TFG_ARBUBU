from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from import_export import resources
import csv
from django.http.response import HttpResponse

from django.template import RequestContext, Template, Context

from django.template.loader import get_template

from django.views.generic import ListView, TemplateView, CreateView

from django.contrib import auth

from .models import Usuario, Familia, Genero, Especie, Individuos

from .forms import SignUpForm

from django.contrib.auth.views import LoginView, LogoutView

from tablib import Dataset

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side

from .admin import IndividuoResource

class ListaGeneros(ListView):

    template_name = "pantallaPrincipal/lista-generos.html"
    model = Genero
    context_object_name = 'genero'

    def get_queryset(self):
        id = self.kwargs['pk']
        lista = Individuos.objects.filter(
            idGenero=id
        )
        # devuelvo el resultado o la lista resultado
        return lista

#class exportarExcel(TemplateView):
#    def get(self, request, *args, **kwargs):
#        query = Individuos.objects.all()
#        wb = Workbook()

#        nombreArchivo = "datosIndividuos.xlsx"
#        response = HttpResponse(content_type = "application/ms-excel")
#        contenido = "attachment; filename = {0}".format(nombreArchivo)
#        response["Content-Disposition"] = contenido
#        wb.save()
#        return response

class IndexView(TemplateView):

    template_name = "principal/index.html"

class Familias(ListView):

    template_name = "principal/familias.html"
    model = Familia
    context_object_name = 'familia'

class Sambucus(ListView):

    template_name = "principal/sambucus.html"
    model = Genero
    context_object_name = 'sambucus'

class SambucusNigra(ListView):

    template_name = "principal/sambucusNigra.html"
    model = Especie
    context_object_name = 'sambucusNigra'

class Sauco(ListView):

    template_name = "principal/sauco.html"
    model = Individuos
    context_object_name = 'sauco'

class Generos(ListView):

    template_name = "principal/generos.html"
    model = Genero
    context_object_name = 'genero'

class Especies(ListView):

    template_name = "principal/especies.html"
    model = Especie
    context_object_name = 'especie'

class CirueloRojo(ListView):

    template_name = "principal/cirueloRojo.html"
    model = Individuos
    context_object_name = 'cirueloRojo'

class Pinsapo(ListView):

    template_name = "principal/pinsapo.html"
    model = Individuos
    context_object_name = 'pinsapo'

class Olivo(ListView):

    template_name = "principal/olivo.html"
    model = Individuos
    context_object_name = 'olivo'

class Acebo(ListView):

    template_name = "principal/acebo.html"
    model = Individuos
    context_object_name = 'acebo'

class Catalpa(ListView):

    template_name = "principal/catalpa.html"
    model = Individuos
    context_object_name = 'catalpa'

def importar(request):

   if request.method == 'POST':

     individuos_resource = IndividuoResource()
     dataset = Dataset()
     nuevos_individuos = request.FILES['xlsfile']
     imported_data = dataset.load(nuevos_individuos.read())
     result = individuos_resource.import_data(dataset, dry_run=True) # Test the data import
     if not result.has_errors():
       individuos_resource.import_data(dataset, dry_run=False) # Actually import now

   return render(request, 'principal/importar.html')

class Individuos(ListView):

    model = Individuos
    context_object_name = 'individuo'
    template_name = "principal/individuos.html"



class SignUpView(CreateView):
    model = Usuario
    form_class = SignUpForm

    def form_valid(self, form):
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/index')

class SignInView(LoginView):
    template_name = 'principal/iniciar_sesion.html'

class SignOutView(LogoutView):
    pass


#def some_view(request):
    # Create the HttpResponse object with the appropriate CSV header.
#    response = HttpResponse(content_type='text/csv')
#    response['Content-Disposition'] = 'attachment; filename="exportar.csv"'

#    writer = csv.writer(response)
#    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
#    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

#    return response



def individuo_print(self, pk=None):
   import io
   from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
   from reportlab.lib.styles import getSampleStyleSheet
   from reportlab.lib import colors
   from reportlab.lib.pagesizes import letter
   from reportlab.platypus import Table

   response = HttpResponse(content_type='application/pdf')
   buff = io.BytesIO()
   doc = SimpleDocTemplate(buff,
               pagesize=letter,
               rightMargin=40,
               leftMargin=40,
               topMargin=60,
               bottomMargin=18,
               )
   individuos = []
   styles = getSampleStyleSheet()
   header = Paragraph("Listado de Individuos", styles['Heading1'])
   individuos.append(header)
   headings = ('idIndividuo', 'nombreComun', 'especie', 'motivoSingular','explicacionMotivoSingular','latitud','longitud','ubicacion','altura','perimetro')

   todascategorias = [(p.idIndividuo, p.nombreComun, p.especie.nombreComunEspecie, p.motivoSingular, p.explicacionMotivoSingular, p.latitud,p.longitud,p.ubicacion,p.altura,p.perimetro)
               for p in Individuos.objects.all()]
   t = Table([headings] + todascategorias)
   t.setStyle(TableStyle(
     [
       ('GRID', (0, 0), (3, -1), 1, colors.dodgerblue),
       ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
       ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
     ]
   ))

   individuos.append(t)
   doc.build(individuos)
   response.write(buff.getvalue())
   buff.close()
   return response
