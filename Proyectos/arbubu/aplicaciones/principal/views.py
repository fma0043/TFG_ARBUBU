from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from import_export import resources
import csv
from django.http.response import HttpResponse, HttpResponseRedirect

from django.template import RequestContext, Template, Context

from django.template.loader import get_template

from django.views.generic import ListView, TemplateView, CreateView

from django.contrib import auth

from .models import Usuario, Familia, Genero, Especie, Individuos
from .models import Individuos as IndividuosModel

from .forms import SignUpForm, IndividuosForm
from django.shortcuts import render_to_response

from django.contrib.auth.views import LoginView, LogoutView

from tablib import Dataset

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side

import io
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import Table


def addIndividuo(request):
    if request.method == 'POST':
        formulario = IndividuosForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/index')
    else:
        formulario = IndividuosForm()
    return render(request,'principal/addIndividuo.html',{'formulario':formulario})

class IndexView(TemplateView):

    template_name = "principal/index.html"

class Adoxaceas(ListView):

    template_name = "principal/familias/adoxaceas.html"
    model = Familia
    context_object_name = 'adoxaceas'

class Aquifoliaceas(ListView):

    template_name = "principal/familias/aquifoliaceas.html"
    model = Familia
    context_object_name = 'aquifoliaceas'

class Araliaceas(ListView):

    template_name = "principal/familias/araliaceas.html"
    model = Familia
    context_object_name = 'araliaceas'

class Bignoniaceas(ListView):

    template_name = "principal/familias/bignoniaceas.html"
    model = Familia
    context_object_name = 'bignoniaceas'

class Caprifoliaceas(ListView):

    template_name = "principal/familias/caprifoliaceas.html"
    model = Familia
    context_object_name = 'caprifoliaceas'

class Cupresaceas(ListView):

    template_name = "principal/familias/cupresaceas.html"
    model = Familia
    context_object_name = 'cupresaceas'

class Fabaceaes(ListView):

    template_name = "principal/familias/fabaceaes.html"
    model = Familia
    context_object_name = 'fabaceaes'

class Fagaceas(ListView):

    template_name = "principal/familias/fagaceas.html"
    model = Familia
    context_object_name = 'fagaceas'

class Juglandaceas(ListView):

    template_name = "principal/familias/juglandaceas.html"
    model = Familia
    context_object_name = 'juglandaceas'

class Leguminosas(ListView):

    template_name = "principal/familias/leguminosas.html"
    model = Familia
    context_object_name = 'leguminosas'

class Magnoliaceas(ListView):

    template_name = "principal/familias/magnoliaceas.html"
    model = Familia
    context_object_name = 'magnoliaceas'

class Malvaceae(ListView):

    template_name = "principal/familias/malvaceae.html"
    model = Familia
    context_object_name = 'malvaceae'

class Moraceas(ListView):

    template_name = "principal/familias/moraceas.html"
    model = Familia
    context_object_name = 'moraceas'

class Oleaceas(ListView):

    template_name = "principal/familias/oleaceas.html"
    model = Familia
    context_object_name = 'oleaceas'

class Pinaceas(ListView):

    template_name = "principal/familias/pinaceas.html"
    model = Familia
    context_object_name = 'pinaceas'

class Platanaceas(ListView):

    template_name = "principal/familias/platanaceas.html"
    model = Familia
    context_object_name = 'platanaceas'

class Rosaceas(ListView):

    template_name = "principal/familias/rosaceas.html"
    model = Familia
    context_object_name = 'rosaceas'

class Salicaceas(ListView):

    template_name = "principal/familias/salicaceas.html"
    model = Familia
    context_object_name = 'salicaceas'

class Simaroubaceas(ListView):

    template_name = "principal/familias/simaroubaceas.html"
    model = Familia
    context_object_name = 'simaroubaceas'

class Tamariacaceas(ListView):

    template_name = "principal/familias/tamariacaceas.html"
    model = Familia
    context_object_name = 'tamariacaceas'

class Taxaceas(ListView):

    template_name = "principal/familias/taxaceas.html"
    model = Familia
    context_object_name = 'taxaceas'

class Tiliaceas(ListView):

    template_name = "principal/familias/tiliaceas.html"
    model = Familia
    context_object_name = 'tiliaceas'

class Ulmaceas(ListView):

    template_name = "principal/familias/ulmaceas.html"
    model = Familia
    context_object_name = 'ulmaceas'

class Familias(ListView):

    template_name = "principal/familias.html"
    model = Familia
    context_object_name = 'familia'

class Abies(ListView):

    template_name = "principal/generos/abies.html"
    model = Genero
    context_object_name = 'abies'

class Ailanthus(ListView):

    template_name = "principal/generos/ailanthus.html"
    model = Genero
    context_object_name = 'ailanthus'

class CatalpaG(ListView):

    template_name = "principal/generos/catalpaG.html"
    model = Genero
    context_object_name = 'catalpaG'

class Cedrus(ListView):

    template_name = "principal/generos/cedrus.html"
    model = Genero
    context_object_name = 'cedrus'

class Cercis(ListView):

    template_name = "principal/generos/cercis.html"
    model = Genero
    context_object_name = 'cercis'

class Cupressus(ListView):

    template_name = "principal/generos/cupressus.html"
    model = Genero
    context_object_name = 'cupressus'

class Fagus(ListView):

    template_name = "principal/generos/fagus.html"
    model = Genero
    context_object_name = 'fagus'

class Ficus(ListView):

    template_name = "principal/generos/ficus.html"
    model = Genero
    context_object_name = 'ficus'

class Hedera(ListView):

    template_name = "principal/generos/hedera.html"
    model = Genero
    context_object_name = 'hedera'

class Hibiscus(ListView):

    template_name = "principal/generos/hibiscus.html"
    model = Genero
    context_object_name = 'hibiscus'

class Ilex(ListView):

    template_name = "principal/generos/ilex.html"
    model = Genero
    context_object_name = 'ilex'

class Juglans(ListView):

    template_name = "principal/generos/juglans.html"
    model = Genero
    context_object_name = 'juglans'

class Laburnum(ListView):

    template_name = "principal/generos/laburnum.html"
    model = Genero
    context_object_name = 'laburnum'

class Ligustrum(ListView):

    template_name = "principal/generos/ligustrum.html"
    model = Genero
    context_object_name = 'ligustrum'

class Liriodendron(ListView):

    template_name = "principal/generos/liriodendron.html"
    model = Genero
    context_object_name = 'liriodendron'

class Lonicera(ListView):

    template_name = "principal/generos/lonicera.html"
    model = Genero
    context_object_name = 'lonicera'

class Morus(ListView):

    template_name = "principal/generos/morus.html"
    model = Genero
    context_object_name = 'morus'

class Olea(ListView):

    template_name = "principal/generos/olea.html"
    model = Genero
    context_object_name = 'olea'

class Picea(ListView):

    template_name = "principal/generos/picea.html"
    model = Genero
    context_object_name = 'picea'

class Pinus(ListView):

    template_name = "principal/generos/pinus.html"
    model = Genero
    context_object_name = 'pinus'

class Platanus(ListView):

    template_name = "principal/generos/platanus.html"
    model = Genero
    context_object_name = 'platanus'

class Platycladus(ListView):

    template_name = "principal/generos/platycladus.html"
    model = Genero
    context_object_name = 'platycladus'

class Populus(ListView):

    template_name = "principal/generos/populus.html"
    model = Genero
    context_object_name = 'populus'

class Prunus(ListView):

    template_name = "principal/generos/prunus.html"
    model = Genero
    context_object_name = 'prunus'

class Pyrus(ListView):

    template_name = "principal/generos/pyrus.html"
    model = Genero
    context_object_name = 'pyrus'

class Quercus(ListView):

    template_name = "principal/generos/quercus.html"
    model = Genero
    context_object_name = 'quercus'

class Robinia(ListView):

    template_name = "principal/generos/robinia.html"
    model = Genero
    context_object_name = 'robinia'

class Salix(ListView):

    template_name = "principal/generos/salix.html"
    model = Genero
    context_object_name = 'salix'

class Sambucus(ListView):

    template_name = "principal/generos/sambucus.html"
    model = Genero
    context_object_name = 'sambucus'

class Sequoiadendron(ListView):

    template_name = "principal/generos/sequoiadendron.html"
    model = Genero
    context_object_name = 'sequoiadendron'

class Syringa(ListView):

    template_name = "principal/generos/syringa.html"
    model = Genero
    context_object_name = 'syringa'

class Tamarix(ListView):

    template_name = "principal/generos/tamarix.html"
    model = Genero
    context_object_name = 'tamarix'

class Taxus(ListView):

    template_name = "principal/generos/taxus.html"
    model = Genero
    context_object_name = 'taxus'

class Thuja(ListView):

    template_name = "principal/generos/thuja.html"
    model = Genero
    context_object_name = 'thuja'

class Tilia(ListView):

    template_name = "principal/generos/tilia.html"
    model = Genero
    context_object_name = 'tilia'

class Ulmus(ListView):

    template_name = "principal/generos/ulmus.html"
    model = Genero
    context_object_name = 'ulmus'

class AbiesAlba(ListView):

    template_name = "principal/especies/abiesAlba.html"
    model = Especie
    context_object_name = 'abiesAlba'

class AbiesPinsapo(ListView):

    template_name = "principal/especies/abiesPinsapo.html"
    model = Especie
    context_object_name = 'abiesPinsapo'

class AilanthusAltissima(ListView):

    template_name = "principal/especies/ailanthusAltissima.html"
    model = Especie
    context_object_name = 'ailanthusAltissima'

class CatalpaBignonioides(ListView):

    template_name = "principal/especies/catalpaBignonioides.html"
    model = Especie
    context_object_name = 'catalpaBignonioides'

class CedrusAtlantica(ListView):

    template_name = "principal/especies/cedrusAtlantica.html"
    model = Especie
    context_object_name = 'cedrusAtlantica'

class CedrusDeodara(ListView):

    template_name = "principal/especies/cedrusDeodara.html"
    model = Especie
    context_object_name = 'cedrusDeodara'

class CedrusAtlanticaGlaucaPendula(ListView):

    template_name = "principal/especies/cedrusAtlanticaGlaucaPendula.html"
    model = Especie
    context_object_name = 'cedrusAtlanticaGlaucaPendula'

class CercisSiliquastrum(ListView):

    template_name = "principal/especies/cercisSiliquastrum.html"
    model = Especie
    context_object_name = 'cercisSiliquastrum'

class CupressusArizonica(ListView):

    template_name = "principal/especies/cupressusArizonica.html"
    model = Especie
    context_object_name = 'cupressusArizonica'

class FagusSylvatica(ListView):

    template_name = "principal/especies/fagusSylvatica.html"
    model = Especie
    context_object_name = 'fagusSylvatica'

class FagusSylvaticacvAtropunicea(ListView):

    template_name = "principal/especies/fagusSylvaticacvAtropunicea.html"
    model = Especie
    context_object_name = 'fagusSylvaticacvAtropunicea'

class FicusCarica(ListView):

    template_name = "principal/especies/ficusCarica.html"
    model = Especie
    context_object_name = 'ficusCarica'

class HederaHelix(ListView):

    template_name = "principal/especies/hederaHelix.html"
    model = Especie
    context_object_name = 'hederaHelix'

class HibiscusSyriacus(ListView):

    template_name = "principal/especies/hibiscusSyriacus.html"
    model = Especie
    context_object_name = 'hibiscusSyriacus'

class IlexAquifolium(ListView):

    template_name = "principal/especies/ilexAquifolium.html"
    model = Especie
    context_object_name = 'ilexAquifolium'

class JuglansRegia(ListView):

    template_name = "principal/especies/juglansRegia.html"
    model = Especie
    context_object_name = 'juglansRegia'

class LaburnumAnagyroides(ListView):

    template_name = "principal/especies/laburnumAnagyroides.html"
    model = Especie
    context_object_name = 'laburnumAnagyroides'

class LigustrumLucidum(ListView):

    template_name = "principal/especies/ligustrumLucidum.html"
    model = Especie
    context_object_name = 'ligustrumLucidum'

class LiriodendronTulipifera(ListView):

    template_name = "principal/especies/liriodendronTulipifera.html"
    model = Especie
    context_object_name = 'liriodendronTulipifera'

class LoniceraSpp(ListView):

    template_name = "principal/especies/loniceraSpp.html"
    model = Especie
    context_object_name = 'loniceraSpp'

class MorusNigra(ListView):

    template_name = "principal/especies/morusNigra.html"
    model = Especie
    context_object_name = 'morusNigra'

class OleaEuropaea(ListView):

    template_name = "principal/especies/oleaEuropaea.html"
    model = Especie
    context_object_name = 'oleaEuropaea'

class PiceaAbies(ListView):

    template_name = "principal/especies/piceaAbies.html"
    model = Especie
    context_object_name = 'piceaAbies'

class PinusPicea(ListView):

    template_name = "principal/especies/pinusPicea.html"
    model = Especie
    context_object_name = 'pinusPicea'

class PlatanusxHispanica(ListView):

    template_name = "principal/especies/platanusxHispanica.html"
    model = Especie
    context_object_name = 'platanusxHispanica'

class PlatycladusOrientalis(ListView):

    template_name = "principal/especies/platycladusOrientalis.html"
    model = Especie
    context_object_name = 'platycladusOrientalis'

class PopulusAlba(ListView):

    template_name = "principal/especies/populusAlba.html"
    model = Especie
    context_object_name = 'populusAlba'

class PopulusNigra(ListView):

    template_name = "principal/especies/populusNigra.html"
    model = Especie
    context_object_name = 'populusNigra'

class PopulusSimonii(ListView):

    template_name = "principal/especies/populusSimonii.html"
    model = Especie
    context_object_name = 'populusSimonii'

class PopulusxCanadensis(ListView):

    template_name = "principal/especies/populusxCanadensis.html"
    model = Especie
    context_object_name = 'populusxCanadensis'

class PrunusCerasiferavarPissardii(ListView):

    template_name = "principal/especies/prunusCerasiferavarPissardii.html"
    model = Especie
    context_object_name = 'prunusCerasiferavarPissardii'

class PrunusLaurocerasus(ListView):

    template_name = "principal/especies/prunusLaurocerasus.html"
    model = Especie
    context_object_name = 'prunusLaurocerasus'

class PyrusCommunis(ListView):

    template_name = "principal/especies/pyrusCommunis.html"
    model = Especie
    context_object_name = 'pyrusCommunis'

class QuercusFaginea(ListView):

    template_name = "principal/especies/quercusFaginea.html"
    model = Especie
    context_object_name = 'quercusFaginea'

class QuercusIlex(ListView):

    template_name = "principal/especies/quercusIlex.html"
    model = Especie
    context_object_name = 'quercusIlex'

class RobiniaPseudoacacia(ListView):

    template_name = "principal/especies/robiniaPseudoacacia.html"
    model = Especie
    context_object_name = 'robiniaPseudoacacia'

class SalixBabylonica(ListView):

    template_name = "principal/especies/salixBabylonica.html"
    model = Especie
    context_object_name = 'salixBabylonica'

class SambucusNigra(ListView):

    template_name = "principal/especies/sambucusNigra.html"
    model = Especie
    context_object_name = 'sambucusNigra'

class SequoiadendronGiganteum(ListView):

    template_name = "principal/especies/sequoiadendronGiganteum.html"
    model = Especie
    context_object_name = 'sequoiadendronGiganteum'

class SyringaVulgaris(ListView):

    template_name = "principal/especies/syringaVulgaris.html"
    model = Especie
    context_object_name = 'syringaVulgaris'

class TamarixSpp(ListView):

    template_name = "principal/especies/tamarixSpp.html"
    model = Especie
    context_object_name = 'tamarixSpp'

class TaxusBaccata(ListView):

    template_name = "principal/especies/taxusBaccata.html"
    model = Especie
    context_object_name = 'taxusBaccata'

class ThujaOccidentalis(ListView):

    template_name = "principal/especies/thujaOccidentalis.html"
    model = Especie
    context_object_name = 'thujaOccidentalis'

class ThujaPlicata(ListView):

    template_name = "principal/especies/thujaPlicata.html"
    model = Especie
    context_object_name = 'thujaPlicata'

class TiliaSpp(ListView):

    template_name = "principal/especies/tiliaSpp.html"
    model = Especie
    context_object_name = 'tiliaSpp'

class UlmusPumila(ListView):

    template_name = "principal/especies/ulmusPumila.html"
    model = Especie
    context_object_name = 'ulmusPumila'

class XCupressocyparisLeylandii(ListView):

    template_name = "principal/especies/xCupressocyparisLeylandii.html"
    model = Especie
    context_object_name = 'xCupressocyparisLeylandii'

class Generos(ListView):

    template_name = "principal/generos.html"
    model = Genero
    context_object_name = 'genero'

class Especies(ListView):

    template_name = "principal/especies.html"
    model = Especie
    context_object_name = 'especie'

class Hiedra1(ListView):

    template_name = "principal/individuos/hiedra1.html"
    model = Individuos
    context_object_name = 'hiedra1'

class Higuera(ListView):

    template_name = "principal/individuos/higuera.html"
    model = Individuos
    context_object_name = 'higuera'

class LaurelCerezo1(ListView):

    template_name = "principal/individuos/laurelCerezo1.html"
    model = Individuos
    context_object_name = 'laurelCerezo1'

class LaurelCerezo2(ListView):

    template_name = "principal/individuos/laurelCerezo2.html"
    model = Individuos
    context_object_name = 'laurelCerezo2'

class Lilo1(ListView):

    template_name = "principal/individuos/lilo1.html"
    model = Individuos
    context_object_name = 'lilo1'

class Lilo2(ListView):

    template_name = "principal/individuos/lilo2.html"
    model = Individuos
    context_object_name = 'lilo2'

class Madreselva(ListView):

    template_name = "principal/individuos/madreselva.html"
    model = Individuos
    context_object_name = 'madreselva'

class Moral(ListView):

    template_name = "principal/individuos/moral.html"
    model = Individuos
    context_object_name = 'moral'

class Moribundo(ListView):

    template_name = "principal/individuos/moribundo.html"
    model = Individuos
    context_object_name = 'moribundo'

class Nogal1(ListView):

    template_name = "principal/individuos/nogal1.html"
    model = Individuos
    context_object_name = 'nogal1'

class Nogal2(ListView):

    template_name = "principal/individuos/nogal2.html"
    model = Individuos
    context_object_name = 'nogal2'

class Hiedra2(ListView):

    template_name = "principal/individuos/hiedra2.html"
    model = Individuos
    context_object_name = 'hiedra2'

class AlamoBlanco1(ListView):

    template_name = "principal/individuos/alamoBlanco1.html"
    model = Individuos
    context_object_name = 'alamoBlanco1'

class AlamoBlanco2(ListView):

    template_name = "principal/individuos/alamoBlanco2.html"
    model = Individuos
    context_object_name = 'alamoBlanco2'

class AligustreJapon1(ListView):

    template_name = "principal/individuos/aligustreJapon1.html"
    model = Individuos
    context_object_name = 'aligustreJapon1'

class AligustreJapon2(ListView):

    template_name = "principal/individuos/aligustreJapon2.html"
    model = Individuos
    context_object_name = 'aligustreJapon2'

class AligustreJapon3(ListView):

    template_name = "principal/individuos/aligustreJapon3.html"
    model = Individuos
    context_object_name = 'aligustreJapon3'

class ArbolTulipanes(ListView):

    template_name = "principal/individuos/arbolTulipanes.html"
    model = Individuos
    context_object_name = 'arbolTulipanes'

class ArbolAmor(ListView):

    template_name = "principal/individuos/arbolAmor.html"
    model = Individuos
    context_object_name = 'arbolAmor'

class Ailanto1(ListView):

    template_name = "principal/individuos/ailanto1.html"
    model = Individuos
    context_object_name = 'ailanto1'

class Ailanto2(ListView):

    template_name = "principal/individuos/ailanto2.html"
    model = Individuos
    context_object_name = 'ailanto2'

class Ailanto3(ListView):

    template_name = "principal/individuos/ailanto3.html"
    model = Individuos
    context_object_name = 'ailanto3'

class AlamoChino1(ListView):

    template_name = "principal/individuos/alamoChino1.html"
    model = Individuos
    context_object_name = 'alamoChino1'

class AlamoChino2(ListView):

    template_name = "principal/individuos/alamoChino2.html"
    model = Individuos
    context_object_name = 'alamoChino2'

class AlamoChino3(ListView):

    template_name = "principal/individuos/alamoChino3.html"
    model = Individuos
    context_object_name = 'alamoChino3'

class AlamoChino4(ListView):

    template_name = "principal/individuos/alamoChino4.html"
    model = Individuos
    context_object_name = 'alamoChino4'

class Acebo1(ListView):

    template_name = "principal/individuos/acebo1.html"
    model = Individuos
    context_object_name = 'acebo1'

class Acebo2(ListView):

    template_name = "principal/individuos/acebo2.html"
    model = Individuos
    context_object_name = 'acebo2'


class Sauco(ListView):

    template_name = "principal/individuos/sauco.html"
    model = Individuos
    context_object_name = 'sauco'

class CirueloRojo1(ListView):

    template_name = "principal/individuos/cirueloRojo1.html"
    model = Individuos
    context_object_name = 'cirueloRojo1'

class CirueloRojo2(ListView):

    template_name = "principal/individuos/cirueloRojo2.html"
    model = Individuos
    context_object_name = 'cirueloRojo2'

class CirueloRojo3(ListView):

    template_name = "principal/individuos/cirueloRojo3.html"
    model = Individuos
    context_object_name = 'cirueloRojo3'

class CirueloRojo4(ListView):

    template_name = "principal/individuos/cirueloRojo4.html"
    model = Individuos
    context_object_name = 'cirueloRojo4'

class Encina(ListView):

    template_name = "principal/individuos/encina.html"
    model = Individuos
    context_object_name = 'encina'

class FalsoEbano(ListView):

    template_name = "principal/individuos/falsoEbano.html"
    model = Individuos
    context_object_name = 'falsoEbano'

class Haya(ListView):

    template_name = "principal/individuos/haya.html"
    model = Individuos
    context_object_name = 'haya'

class HayaPurpura(ListView):

    template_name = "principal/individuos/hayaPurpura.html"
    model = Individuos
    context_object_name = 'hayaPurpura'

class FalsaAcacia1(ListView):

    template_name = "principal/individuos/falsaAcacia1.html"
    model = Individuos
    context_object_name = 'falsaAcacia1'

class FalsaAcacia2(ListView):

    template_name = "principal/individuos/falsaAcacia2.html"
    model = Individuos
    context_object_name = 'falsaAcacia2'

class AbetoRojo1(ListView):

    template_name = "principal/individuos/abetoRojo1.html"
    model = Individuos
    context_object_name = 'abetoRojo1'

class AbetoRojo2(ListView):

    template_name = "principal/individuos/abetoRojo2.html"
    model = Individuos
    context_object_name = 'abetoRojo2'

class AbetoRojo3(ListView):

    template_name = "principal/individuos/abetoRojo3.html"
    model = Individuos
    context_object_name = 'abetoRojo3'

class AbetoRojo4(ListView):

    template_name = "principal/individuos/abetoRojo4.html"
    model = Individuos
    context_object_name = 'abetoRojo4'

class AbetoRojo5(ListView):

    template_name = "principal/individuos/abetoRojo5.html"
    model = Individuos
    context_object_name = 'abetoRojo5'

class AbetoRojo6(ListView):

    template_name = "principal/individuos/abetoRojo6.html"
    model = Individuos
    context_object_name = 'abetoRojo6'

class AbetoRojo7(ListView):

    template_name = "principal/individuos/abetoRojo7.html"
    model = Individuos
    context_object_name = 'abetoRojo7'

class AbetoRojo8(ListView):

    template_name = "principal/individuos/abetoRojo8.html"
    model = Individuos
    context_object_name = 'abetoRojo8'

class Pinsapo1(ListView):

    template_name = "principal/individuos/pinsapo1.html"
    model = Individuos
    context_object_name = 'pinsapo1'

class Pinsapo2(ListView):

    template_name = "principal/individuos/pinsapo2.html"
    model = Individuos
    context_object_name = 'pinsapo2'

class Pinsapo3(ListView):

    template_name = "principal/individuos/pinsapo3.html"
    model = Individuos
    context_object_name = 'pinsapo3'

class Pinsapo4(ListView):

    template_name = "principal/individuos/pinsapo4.html"
    model = Individuos
    context_object_name = 'pinsapo4'

class Olivo(ListView):

    template_name = "principal/individuos/olivo.html"
    model = Individuos
    context_object_name = 'olivo'

class OlmoSiberiano1(ListView):

    template_name = "principal/individuos/olmoSiberiano1.html"
    model = Individuos
    context_object_name = 'olmoSiberiano1'

class OlmoSiberiano2(ListView):

    template_name = "principal/individuos/olmoSiberiano2.html"
    model = Individuos
    context_object_name = 'olmoSiberiano2'

class Peral(ListView):

    template_name = "principal/individuos/peral.html"
    model = Individuos
    context_object_name = 'peral'

class PinoPinonero1(ListView):

    template_name = "principal/individuos/pinoPinonero1.html"
    model = Individuos
    context_object_name = 'pinoPinonero1'

class PinoPinonero2(ListView):

    template_name = "principal/individuos/pinoPinonero2.html"
    model = Individuos
    context_object_name = 'pinoPinonero2'

class PinoPinonero3(ListView):

    template_name = "principal/individuos/pinoPinonero3.html"
    model = Individuos
    context_object_name = 'pinoPinonero3'

class PinoPinonero4(ListView):

    template_name = "principal/individuos/pinoPinonero4.html"
    model = Individuos
    context_object_name = 'pinoPinonero4'

class PinoPinonero5(ListView):

    template_name = "principal/individuos/pinoPinonero5.html"
    model = Individuos
    context_object_name = 'pinoPinonero5'

class PlatanoSombra1(ListView):

    template_name = "principal/individuos/platanoSombra1.html"
    model = Individuos
    context_object_name = 'platanoSombra1'

class PlatanoSombra1(ListView):

    template_name = "principal/individuos/platanoSombra1.html"
    model = Individuos
    context_object_name = 'platanoSombra1'

class PlatanoSombra2(ListView):

    template_name = "principal/individuos/platanoSombra2.html"
    model = Individuos
    context_object_name = 'platanoSombra2'

class PlatanoSombra3(ListView):

    template_name = "principal/individuos/platanoSombra3.html"
    model = Individuos
    context_object_name = 'platanoSombra3'

class PlatanoSombra4(ListView):

    template_name = "principal/individuos/platanoSombra4.html"
    model = Individuos
    context_object_name = 'platanoSombra4'

class PlatanoSombra5(ListView):

    template_name = "principal/individuos/platanoSombra5.html"
    model = Individuos
    context_object_name = 'platanoSombra5'

class PlatanoSombra6(ListView):

    template_name = "principal/individuos/platanoSombra6.html"
    model = Individuos
    context_object_name = 'platanoSombra6'

class PlatanoSombra7(ListView):

    template_name = "principal/individuos/platanoSombra7.html"
    model = Individuos
    context_object_name = 'platanoSombra7'

class Quejigo(ListView):

    template_name = "principal/individuos/quejigo.html"
    model = Individuos
    context_object_name = 'quejigo'

class RosaDeSiria(ListView):

    template_name = "principal/individuos/rosaDeSiria.html"
    model = Individuos
    context_object_name = 'rosaDeSiria'


class SauceLloron1(ListView):

    template_name = "principal/individuos/sauceLloron1.html"
    model = Individuos
    context_object_name = 'sauceLloron1'

class SauceLloron2(ListView):

    template_name = "principal/individuos/sauceLloron2.html"
    model = Individuos
    context_object_name = 'sauceLloron2'

class SauceLloron3(ListView):

    template_name = "principal/individuos/sauceLloron3.html"
    model = Individuos
    context_object_name = 'sauceLloron3'

class SauceLloron4(ListView):

    template_name = "principal/individuos/sauceLloron4.html"
    model = Individuos
    context_object_name = 'sauceLloron4'

class SecuoyaGigante(ListView):

    template_name = "principal/individuos/secuoyaGigante.html"
    model = Individuos
    context_object_name = 'secuoyaGigante'

class Taray1(ListView):

    template_name = "principal/individuos/taray1.html"
    model = Individuos
    context_object_name = 'taray1'

class Taray2(ListView):

    template_name = "principal/individuos/taray2.html"
    model = Individuos
    context_object_name = 'taray2'

class Tejo1(ListView):

    template_name = "principal/individuos/tejo1.html"
    model = Individuos
    context_object_name = 'tejo1'

class Tejo2(ListView):

    template_name = "principal/individuos/tejo2.html"
    model = Individuos
    context_object_name = 'tejo2'

class Tilo1(ListView):

    template_name = "principal/individuos/tilo1.html"
    model = Individuos
    context_object_name = 'tilo1'

class Tilo2(ListView):

    template_name = "principal/individuos/tilo2.html"
    model = Individuos
    context_object_name = 'tilo2'

class TuyaGigante1(ListView):

    template_name = "principal/individuos/tuyaGigante1.html"
    model = Individuos
    context_object_name = 'tuyaGigante1'

class TuyaGigante2(ListView):

    template_name = "principal/individuos/tuyaGigante2.html"
    model = Individuos
    context_object_name = 'tuyaGigante2'

class TuyaOriental(ListView):

    template_name = "principal/individuos/tuyaOriental.html"
    model = Individuos
    context_object_name = 'tuyaOriental'

class TuyaCanada1(ListView):

    template_name = "principal/individuos/tuyaCanada1.html"
    model = Individuos
    context_object_name = 'tuyaCanada1'

class TuyaCanada2(ListView):

    template_name = "principal/individuos/tuyaCanada2.html"
    model = Individuos
    context_object_name = 'tuyaCanada2'

class TuyaCanada3(ListView):

    template_name = "principal/individuos/tuyaCanada3.html"
    model = Individuos
    context_object_name = 'tuyaCanada3'

class Chopo(ListView):

    template_name = "principal/individuos/chopo.html"
    model = Individuos
    context_object_name = 'chopo'

class CipresArizona1(ListView):

    template_name = "principal/individuos/cipresArizona1.html"
    model = Individuos
    context_object_name = 'cipresArizona1'

class CipresArizona2(ListView):

    template_name = "principal/individuos/cipresArizona2.html"
    model = Individuos
    context_object_name = 'cipresArizona2'

class CipresLeyland(ListView):

    template_name = "principal/individuos/cipresLeyland.html"
    model = Individuos
    context_object_name = 'cipresLeyland'

class ChopoCanadiense1(ListView):

    template_name = "principal/individuos/chopoCanadiense1.html"
    model = Individuos
    context_object_name = 'chopoCanadiense1'

class ChopoCanadiense2(ListView):

    template_name = "principal/individuos/chopoCanadiense2.html"
    model = Individuos
    context_object_name = 'chopoCanadiense2'

class ChopoCanadiense3(ListView):

    template_name = "principal/individuos/chopoCanadiense3.html"
    model = Individuos
    context_object_name = 'chopoCanadiense3'

class ChopoCanadiense4(ListView):

    template_name = "principal/individuos/chopoCanadiense4.html"
    model = Individuos
    context_object_name = 'chopoCanadiense4'

class CedroAtlas1(ListView):

    template_name = "principal/individuos/cedroAtlas1.html"
    model = Individuos
    context_object_name = 'cedroAtlas1'

class CedroAtlas2(ListView):

    template_name = "principal/individuos/cedroAtlas2.html"
    model = Individuos
    context_object_name = 'cedroAtlas2'

class CedroAtlas3(ListView):

    template_name = "principal/individuos/cedroAtlas3.html"
    model = Individuos
    context_object_name = 'cedroAtlas3'

class CedroAtlas4(ListView):

    template_name = "principal/individuos/cedroAtlas4.html"
    model = Individuos
    context_object_name = 'cedroAtlas4'

class CedroAtlas5(ListView):

    template_name = "principal/individuos/cedroAtlas5.html"
    model = Individuos
    context_object_name = 'cedroAtlas5'

class CedroAtlas6(ListView):

    template_name = "principal/individuos/cedroAtlas6.html"
    model = Individuos
    context_object_name = 'cedroAtlas6'

class CedroAtlas7(ListView):

    template_name = "principal/individuos/cedroAtlas7.html"
    model = Individuos
    context_object_name = 'cedroAtlas7'

class CedroAtlas8(ListView):

    template_name = "principal/individuos/cedroAtlas8.html"
    model = Individuos
    context_object_name = 'cedroAtlas8'

class CedroHimalaya1(ListView):

    template_name = "principal/individuos/cedroHimalaya1.html"
    model = Individuos
    context_object_name = 'cedroHimalaya1'

class CedroHimalaya2(ListView):

    template_name = "principal/individuos/cedroHimalaya2.html"
    model = Individuos
    context_object_name = 'cedroHimalaya2'

class CedroHimalaya3(ListView):

    template_name = "principal/individuos/cedroHimalaya3.html"
    model = Individuos
    context_object_name = 'cedroHimalaya3'

class Catalpa(ListView):

    template_name = "principal/individuos/catalpa.html"
    model = Individuos
    context_object_name = 'catalpa'

class CedroAzul(ListView):

    template_name = "principal/individuos/cedroAzul.html"
    model = Individuos
    context_object_name = 'cedroAzul'

class Abeto1(ListView):

    template_name = "principal/individuos/abeto1.html"
    model = Individuos
    context_object_name = 'abeto1'

class Abeto2(ListView):

    template_name = "principal/individuos/abeto2.html"
    model = Individuos
    context_object_name = 'abeto2'

class IndividuosRioVena(ListView):

    model = Individuos
    context_object_name = 'individuoRioVena'
    template_name = "principal/individuos-rio-vena.html"

class IndividuosHospitalDelRey(ListView):

    model = Individuos
    context_object_name = 'individuoHospitalDelRey'
    template_name = "principal/individuos-hospital-del-rey.html"

class IndividuosHospitalMilitar(ListView):

    model = Individuos
    context_object_name = 'individuoHospitalMilitar'
    template_name = "principal/individuos-hospital-militar.html"

class IndividuosEducacion(ListView):

    model = Individuos
    context_object_name = 'individuoEducacion'
    template_name = "principal/individuos-educacion.html"

class IndividuosCiencias(ListView):

    model = Individuos
    context_object_name = 'individuoCiencias'
    template_name = "principal/individuos-ciencias.html"

def importar(request):

   if request.method == 'POST':

     individuos_resource = IndividuoResource()
     dataset = Dataset()
     nuevos_individuos = request.FILES['xlsfile']
     imported_data = dataset.load(nuevos_individuos.read())
     result = individuos_resource.import_data(dataset, dry_run=True)
     if not result.has_errors():
       individuos_resource.import_data(dataset, dry_run=False)

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

def DescargarIndividuoPdf(self, pk=None):

   response = HttpResponse(content_type='application/pdf')
   buffer = io.BytesIO()
   documento = SimpleDocTemplate(buffer,
               pagesize=landscape(letter),
               rightMargin=20,
               leftMargin=20,
               topMargin=60,
               bottomMargin=20,
               )
   individuos = []
   styles = getSampleStyleSheet()
   header = Paragraph("Listado de Individuos", styles['Heading1'])
   individuos.append(header)
   headings = ('Nombre Comun', 'Especie', 'Motivo Singular', 'Ubicacion','Latitud','Longitud')

   atributos = [(p.nombreComun, p.especie.nombreCientificoEspecie, p.motivoSingular, p.ubicacion, p.latitud,p.longitud)
               for p in IndividuosModel.objects.all()]
   cabecera = Table([headings] + atributos)
   cabecera.setStyle(TableStyle(
     [
       ('GRID', (0, 0), (6, -1), 1, colors.dodgerblue),
       ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
       ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
     ]
   ))

   individuos.append(cabecera)
   documento.build(individuos)
   response.write(buffer.getvalue())
   buffer.close()
   return response
