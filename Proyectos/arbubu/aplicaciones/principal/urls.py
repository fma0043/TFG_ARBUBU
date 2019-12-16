from django.conf.urls import url
from django.urls import include, path, re_path
from . import views,admin
from aplicaciones.principal.views import SignUpView, SignInView, SignOutView, importar, individuo_print

app_name="principal_app"

urlpatterns = [
    path('index', views.IndexView.as_view(),name='index'),
    path('abeto1', views.Abeto1.as_view(),name='abeto1'),
    path('abeto2', views.Abeto2.as_view(),name='abeto2'),
    path('abetoRojo1', views.AbetoRojo1.as_view(),name='abetoRojo1'),
    path('abetoRojo2', views.AbetoRojo2.as_view(),name='abetoRojo2'),
    path('abetoRojo3', views.AbetoRojo3.as_view(),name='abetoRojo3'),
    path('abetoRojo4', views.AbetoRojo4.as_view(),name='abetoRojo4'),
    path('abetoRojo5', views.AbetoRojo5.as_view(),name='abetoRojo5'),
    path('abetoRojo6', views.AbetoRojo6.as_view(),name='abetoRojo6'),
    path('abetoRojo7', views.AbetoRojo7.as_view(),name='abetoRojo7'),
    path('abetoRojo8', views.AbetoRojo8.as_view(),name='abetoRojo8'),
    path('acebo1', views.Acebo1.as_view(),name='acebo1'),
    path('acebo2', views.Acebo2.as_view(),name='acebo2'),
    path('alamoBlanco1', views.AlamoBlanco1.as_view(),name='alamoBlanco1'),
    path('alamoBlanco2', views.AlamoBlanco2.as_view(),name='alamoBlanco2'),
    path('alamoChino1', views.AlamoChino1.as_view(),name='alamoChino1'),
    path('alamoChino2', views.AlamoChino2.as_view(),name='alamoChino2'),
    path('alamoChino3', views.AlamoChino3.as_view(),name='alamoChino3'),
    path('alamoChino4', views.AlamoChino4.as_view(),name='alamoChino4'),
    path('aligustreJapon1', views.AligustreJapon1.as_view(),name='aligustreJapon1'),
    path('aligustreJapon2', views.AligustreJapon2.as_view(),name='aligustreJapon2'),
    path('aligustreJapon3', views.AligustreJapon3.as_view(),name='aligustreJapon3'),
    path('arbolTulipanes', views.ArbolTulipanes.as_view(),name='arbolTulipanes'),
    path('arbolAmor', views.ArbolAmor.as_view(),name='arbolAmor'),
    path('ailanto1', views.Ailanto1.as_view(),name='ailanto1'),
    path('ailanto2', views.Ailanto2.as_view(),name='ailanto2'),
    path('ailanto3', views.Ailanto3.as_view(),name='ailanto3'),
    path('catalpa', views.Catalpa.as_view(), name='catalpa'),
    path('cedroAzul', views.CedroAzul.as_view(),name='cedroAzul'),
    path('cedroHimalaya1', views.CedroHimalaya1.as_view(),name='cedroHimalaya1'),
    path('cedroHimalaya2', views.CedroHimalaya2.as_view(),name='cedroHimalaya2'),
    path('cedroHimalaya3', views.CedroHimalaya3.as_view(),name='cedroHimalaya3'),
    path('cedroAtlas1', views.CedroAtlas1.as_view(),name='cedroAtlas1'),
    path('cedroAtlas2', views.CedroAtlas2.as_view(),name='cedroAtlas2'),
    path('cedroAtlas3', views.CedroAtlas3.as_view(),name='cedroAtlas3'),
    path('cedroAtlas4', views.CedroAtlas4.as_view(),name='cedroAtlas4'),
    path('cedroAtlas5', views.CedroAtlas5.as_view(),name='cedroAtlas5'),
    path('cedroAtlas6', views.CedroAtlas6.as_view(),name='cedroAtlas6'),
    path('cedroAtlas7', views.CedroAtlas7.as_view(),name='cedroAtlas7'),
    path('cedroAtlas8', views.CedroAtlas8.as_view(),name='cedroAtlas8'),
    path('chopo', views.Chopo.as_view(),name='chopo'),
    path('chopoCanadiense1', views.ChopoCanadiense1.as_view(),name='chopoCanadiense1'),
    path('chopoCanadiense2', views.ChopoCanadiense2.as_view(),name='chopoCanadiense2'),
    path('chopoCanadiense3', views.ChopoCanadiense3.as_view(),name='chopoCanadiense3'),
    path('chopoCanadiense4', views.ChopoCanadiense4.as_view(),name='chopoCanadiense4'),
    path('cipresArizona1', views.CipresArizona1.as_view(),name='cipresArizona1'),
    path('cipresArizona2', views.CipresArizona2.as_view(),name='cipresArizona2'),
    path('cipresLeyland', views.CipresLeyland.as_view(),name='cipresLeyland'),
    path('cirueloRojo1', views.CirueloRojo1.as_view(), name='cirueloRojo1'),
    path('cirueloRojo2', views.CirueloRojo2.as_view(), name='cirueloRojo2'),
    path('cirueloRojo3', views.CirueloRojo3.as_view(), name='cirueloRojo3'),
    path('cirueloRojo4', views.CirueloRojo4.as_view(), name='cirueloRojo4'),
    path('encina', views.Encina.as_view(), name='encina'),
    path('falsaAcacia1', views.FalsaAcacia1.as_view(), name='falsaAcacia1'),
    path('falsaAcacia2', views.FalsaAcacia2.as_view(), name='falsaAcacia2'),
    path('falsoEbano', views.FalsoEbano.as_view(), name='falsoEbano'),
    path('haya', views.Haya.as_view(), name='haya'),
    path('hayaPurpura', views.HayaPurpura.as_view(), name='hayaPurpura'),
    path('hiedra1', views.Hiedra1.as_view(),name='hiedra1'),
    path('hiedra2', views.Hiedra2.as_view(),name='hiedra2'),
    path('higuera', views.Higuera.as_view(),name='higuera'),
    path('laurelCerezo1', views.LaurelCerezo1.as_view(),name='laurelCerezo1'),
    path('laurelCerezo2', views.LaurelCerezo2.as_view(),name='laurelCerezo2'),
    path('lilo1', views.Lilo1.as_view(),name='lilo1'),
    path('lilo2', views.Lilo2.as_view(),name='lilo2'),
    path('madreselva', views.Madreselva.as_view(),name='madreselva'),
    path('moral', views.Moral.as_view(),name='moral'),
    path('moribundo', views.Moribundo.as_view(),name='moribundo'),
    path('nogal1', views.Nogal1.as_view(),name='nogal1'),
    path('nogal2', views.Nogal2.as_view(),name='nogal2'),
    path('olivo', views.Olivo.as_view(), name='olivo'),
    path('olmoSiberiano1', views.OlmoSiberiano1.as_view(), name='olmoSiberiano1'),
    path('olmoSiberiano2', views.OlmoSiberiano2.as_view(), name='olmoSiberiano2'),
    path('peral', views.Peral.as_view(), name='peral'),
    path('pinoPinonero1', views.PinoPinonero1.as_view(), name='pinoPinonero1'),
    path('pinoPinonero2', views.PinoPinonero2.as_view(), name='pinoPinonero2'),
    path('pinoPinonero3', views.PinoPinonero3.as_view(), name='pinoPinonero3'),
    path('pinoPinonero4', views.PinoPinonero4.as_view(), name='pinoPinonero4'),
    path('pinoPinonero5', views.PinoPinonero5.as_view(), name='pinoPinonero5'),
    path('pinsapo1', views.Pinsapo1.as_view(), name='pinsapo1'),
    path('pinsapo2', views.Pinsapo2.as_view(), name='pinsapo2'),
    path('pinsapo3', views.Pinsapo3.as_view(), name='pinsapo3'),
    path('pinsapo4', views.Pinsapo4.as_view(), name='pinsapo4'),
    path('platanoSombra1', views.PlatanoSombra1.as_view(), name='platanoSombra1'),
    path('platanoSombra2', views.PlatanoSombra2.as_view(), name='platanoSombra2'),
    path('platanoSombra3', views.PlatanoSombra3.as_view(), name='platanoSombra3'),
    path('platanoSombra4', views.PlatanoSombra4.as_view(), name='platanoSombra4'),
    path('platanoSombra5', views.PlatanoSombra5.as_view(), name='platanoSombra5'),
    path('platanoSombra6', views.PlatanoSombra6.as_view(), name='platanoSombra6'),
    path('platanoSombra7', views.PlatanoSombra7.as_view(), name='platanoSombra7'),
    path('quejigo', views.Quejigo.as_view(), name='quejigo'),
    path('rosaDeSiria', views.RosaDeSiria.as_view(), name='rosaDeSiria'),
    path('sauceLloron1', views.SauceLloron1.as_view(), name='sauceLloron1'),
    path('sauceLloron2', views.SauceLloron2.as_view(), name='sauceLloron2'),
    path('sauceLloron3', views.SauceLloron3.as_view(), name='sauceLloron3'),
    path('sauceLloron4', views.SauceLloron4.as_view(), name='sauceLloron4'),
    path('sauco', views.Sauco.as_view(),name='sauco'),
    path('secuoyaGigante', views.SecuoyaGigante.as_view(),name='secuoyaGigante'),
    path('taray1', views.Taray1.as_view(),name='taray1'),
    path('taray2', views.Taray2.as_view(),name='taray2'),
    path('tejo1', views.Tejo1.as_view(),name='tejo1'),
    path('tejo2', views.Tejo2.as_view(),name='tejo2'),
    path('tilo1', views.Tilo1.as_view(),name='tilo1'),
    path('tilo2', views.Tilo2.as_view(),name='tilo2'),
    path('tuyaGigante1', views.TuyaGigante1.as_view(),name='tuyaGigante1'),
    path('tuyaGigante2', views.TuyaGigante2.as_view(),name='tuyaGigante2'),
    path('tuyaOriental', views.TuyaOriental.as_view(),name='tuyaOriental'),
    path('tuyaCanada1', views.TuyaCanada1.as_view(),name='tuyaCanada1'),
    path('tuyaCanada2', views.TuyaCanada2.as_view(),name='tuyaCanada2'),
    path('tuyaCanada3', views.TuyaCanada3.as_view(),name='tuyaCanada3'),
    path('individuoRioVena', views.IndividuosRioVena.as_view(), name='individuos-rio-vena'),
    path('individuoHospitalDelRey', views.IndividuosHospitalDelRey.as_view(), name='individuos-hospital-del-rey'),
    path('individuoHospitalMilitar', views.IndividuosHospitalMilitar.as_view(), name='individuos-hospital-militar'),
    path('individuoEducacion', views.IndividuosEducacion.as_view(), name='individuos-educacion'),
    path('individuoCiencias', views.IndividuosCiencias.as_view(), name='individuos-ciencias'),
    path('individuos', views.Individuos.as_view(), name='individuos'),
    path('abiesAlba', views.AbiesAlba.as_view(), name='abiesAlba'),
    path('abiesPinsapo', views.AbiesPinsapo.as_view(),name='abiesPinsapo'),
    path('ailanthusAltissima', views.AilanthusAltissima.as_view(),name='ailanthusAltissima'),
    path('catalpaBignonioides', views.CatalpaBignonioides.as_view(),name='catalpaBignonioides'),
    path('cedrusAtlantica', views.CedrusAtlantica.as_view(),name='cedrusAtlantica'),
    path('cedrusDeodara', views.CedrusDeodara.as_view(),name='cedrusDeodara'),
    path('cedrusAtlanticaGlaucaPendula', views.CedrusAtlanticaGlaucaPendula.as_view(),name='cedrusAtlanticaGlaucaPendula'),
    path('cercisSiliquastrum', views.CercisSiliquastrum.as_view(),name='cercisSiliquastrum'),
    path('cupressusArizonica', views.CupressusArizonica.as_view(),name='cupressusArizonica'),
    path('fagusSylvatica', views.FagusSylvatica.as_view(),name='fagusSylvatica'),
    path('fagusSylvaticacvAtropunicea', views.FagusSylvaticacvAtropunicea.as_view(),name='fagusSylvaticacvAtropunicea'),
    path('ficusCarica', views.FicusCarica.as_view(),name='ficusCarica'),
    path('hederaHelix', views.HederaHelix.as_view(),name='hederaHelix'),
    path('hibiscusSyriacus', views.HibiscusSyriacus.as_view(),name='hibiscusSyriacus'),
    path('ilexAquifolium', views.IlexAquifolium.as_view(),name='ilexAquifolium'),
    path('juglansRegia', views.JuglansRegia.as_view(),name='juglansRegia'),
    path('laburnumAnagyroides', views.LaburnumAnagyroides.as_view(),name='laburnumAnagyroides'),
    path('ligustrumLucidum', views.LigustrumLucidum.as_view(),name='ligustrumLucidum'),
    path('liriodendronTulipifera', views.LiriodendronTulipifera.as_view(),name='liriodendronTulipifera'),
    path('loniceraSpp', views.LoniceraSpp.as_view(),name='loniceraSpp'),
    path('morusNigra', views.MorusNigra.as_view(),name='morusNigra'),
    path('oleaEuropaea', views.OleaEuropaea.as_view(),name='oleaEuropaea'),
    path('piceaAbies', views.PiceaAbies.as_view(),name='piceaAbies'),
    path('pinusPicea', views.PinusPicea.as_view(),name='pinusPicea'),
    path('platanusxHispanica', views.PlatanusxHispanica.as_view(),name='platanusxHispanica'),
    path('platycladusOrientalis', views.PlatycladusOrientalis.as_view(),name='platycladusOrientalis'),
    path('populusAlba', views.PopulusAlba.as_view(),name='populusAlba'),
    path('populusNigra', views.PopulusNigra.as_view(),name='populusNigra'),
    path('populusSimonii', views.PopulusSimonii.as_view(),name='populusSimonii'),
    path('populusxCanadensis', views.PopulusxCanadensis.as_view(),name='populusxCanadensis'),
    path('prunusCerasiferavarPissardii', views.PrunusCerasiferavarPissardii.as_view(),name='prunusCerasiferavarPissardii'),
    path('prunusLaurocerasus', views.PrunusLaurocerasus.as_view(),name='prunusLaurocerasus'),
    path('pyrusCommunis', views.PyrusCommunis.as_view(),name='pyrusCommunis'),
    path('quercusFaginea', views.QuercusFaginea.as_view(),name='quercusFaginea'),
    path('quercusIlex', views.QuercusIlex.as_view(),name='quercusIlex'),
    path('robiniaPseudoacacia', views.RobiniaPseudoacacia.as_view(),name='robiniaPseudoacacia'),
    path('salixBabylonica', views.SalixBabylonica.as_view(),name='salixBabylonica'),
    path('sambucusNigra', views.SambucusNigra.as_view(),name='sambucusNigra'),
    path('sequoiadendronGiganteum', views.SequoiadendronGiganteum.as_view(),name='sequoiadendronGiganteum'),
    path('syringaVulgaris', views.SyringaVulgaris.as_view(),name='syringaVulgaris'),
    path('tamarixSpp', views.TamarixSpp.as_view(),name='tamarixSpp'),
    path('taxusBaccata', views.TaxusBaccata.as_view(),name='taxusBaccata'),
    path('thujaOccidentalis', views.ThujaOccidentalis.as_view(),name='thujaOccidentalis'),
    path('thujaPlicata', views.ThujaPlicata.as_view(),name='thujaPlicata'),
    path('tiliaSpp', views.TiliaSpp.as_view(),name='tiliaSpp'),
    path('ulmusPumila', views.UlmusPumila.as_view(),name='ulmusPumila'),
    path('xCupressocyparisLeylandii', views.XCupressocyparisLeylandii.as_view(),name='xCupressocyparisLeylandii'),
    path('especies', views.Especies.as_view(),name='especies'),
    path('abies', views.Abies.as_view(),name='abies'),
    path('ailanthus', views.Ailanthus.as_view(),name='ailanthus'),
    path('catalpaG', views.CatalpaG.as_view(),name='catalpaG'),
    path('cedrus', views.Cedrus.as_view(),name='cedrus'),
    path('cercis', views.Cercis.as_view(),name='cercis'),
    path('cupressus', views.Cupressus.as_view(),name='cupressus'),
    path('fagus', views.Fagus.as_view(),name='fagus'),
    path('ficus', views.Ficus.as_view(),name='ficus'),
    path('hedera', views.Hedera.as_view(),name='hedera'),
    path('hibiscus', views.Hibiscus.as_view(),name='hibiscus'),
    path('ilex', views.Ilex.as_view(),name='ilex'),
    path('juglans', views.Juglans.as_view(),name='juglans'),
    path('laburnum', views.Laburnum.as_view(),name='laburnum'),
    path('ligustrum', views.Ligustrum.as_view(),name='ligustrum'),
    path('liriodendron', views.Liriodendron.as_view(),name='liriodendron'),
    path('lonicera', views.Lonicera.as_view(),name='lonicera'),
    path('morus', views.Morus.as_view(),name='morus'),
    path('olea', views.Olea.as_view(),name='olea'),
    path('picea', views.Picea.as_view(),name='picea'),
    path('pinus', views.Pinus.as_view(),name='pinus'),
    path('platanus', views.Platanus.as_view(),name='platanus'),
    path('platycladus', views.Platycladus.as_view(),name='platycladus'),
    path('populus', views.Populus.as_view(),name='populus'),
    path('prunus', views.Prunus.as_view(),name='prunus'),
    path('pyrus', views.Pyrus.as_view(),name='pyrus'),
    path('quercus', views.Quercus.as_view(),name='quercus'),
    path('robinia', views.Robinia.as_view(),name='robinia'),
    path('salix', views.Salix.as_view(),name='salix'),
    path('sambucus', views.Sambucus.as_view(),name='sambucus'),
    path('sequoiadendron', views.Sequoiadendron.as_view(),name='sequoiadendron'),
    path('syringa', views.Syringa.as_view(),name='syringa'),
    path('tamarix', views.Tamarix.as_view(),name='tamarix'),
    path('taxus', views.Taxus.as_view(),name='taxus'),
    path('thuja', views.Thuja.as_view(),name='thuja'),
    path('tilia', views.Tilia.as_view(),name='tilia'),
    path('ulmus', views.Ulmus.as_view(),name='ulmus'),
    path('generos', views.Generos.as_view(),name='generos'),
    path('adoxaceas', views.Adoxaceas.as_view(),name='adoxaceas'),
    path('aquifoliaceas', views.Aquifoliaceas.as_view(),name='aquifoliaceas'),
    path('araliaceas', views.Araliaceas.as_view(),name='araliaceas'),
    path('bignoniaceas', views.Bignoniaceas.as_view(),name='bignoniaceas'),
    path('caprifoliaceas', views.Caprifoliaceas.as_view(),name='caprifoliaceas'),
    path('cupresaceas', views.Cupresaceas.as_view(),name='cupresaceas'),
    path('fabaceaes', views.Fabaceaes.as_view(),name='fabaceaes'),
    path('fagaceas', views.Fagaceas.as_view(),name='fagaceas'),
    path('juglandaceas', views.Juglandaceas.as_view(),name='juglandaceas'),
    path('leguminosas', views.Leguminosas.as_view(),name='leguminosas'),
    path('magnoliaceas', views.Magnoliaceas.as_view(),name='magnoliaceas'),
    path('malvaceae', views.Malvaceae.as_view(),name='malvaceae'),
    path('moraceas', views.Moraceas.as_view(),name='moraceas'),
    path('oleaceas', views.Oleaceas.as_view(),name='oleaceas'),
    path('pinaceas', views.Pinaceas.as_view(),name='pinaceas'),
    path('platanaceas', views.Platanaceas.as_view(),name='platanaceas'),
    path('rosaceas', views.Rosaceas.as_view(),name='rosaceas'),
    path('salicaceas', views.Salicaceas.as_view(),name='salicaceas'),
    path('simaroubaceas', views.Simaroubaceas.as_view(),name='simaroubaceas'),
    path('tamariacaceas', views.Tamariacaceas.as_view(),name='tamariacaceas'),
    path('taxaceas', views.Taxaceas.as_view(),name='taxaceas'),
    path('tiliaceas', views.Tiliaceas.as_view(),name='tiliaceas'),
    path('ulmaceas', views.Ulmaceas.as_view(),name='ulmaceas'),
    path('familias', views.Familias.as_view(),name='familias'),
    url(r'^registrate/$', views.SignUpView.as_view(), name='sign_up'),
    url(r'^inicia-sesion/$', views.SignInView.as_view(), name='sign_in'),
    url(r'^cerrar-sesion/$', views.SignOutView.as_view(), name='sign_out'),
    path('import', importar, name='import'),
    #path('exportar',exportarExcel.as_view(), name='prueba'),

    #path('export', some_view, name='export'),
    #path('individuos/print', individuo_print, name='individuo_print'),
]
