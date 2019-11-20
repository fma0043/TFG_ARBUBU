from django.conf.urls import url
from django.urls import include, path, re_path
from . import views
from aplicaciones.principal.views import SignUpView, SignInView, SignOutView, importar, individuo_print

app_name="principal_app"

urlpatterns = [
    path('index', views.IndexView.as_view(),name='index'),
    path('familias', views.Familias.as_view(),name='familias'),
    path('generos', views.Generos.as_view(),name='generos'),
    path('especies', views.Especies.as_view(),name='especies'),
    path('individuos', views.Individuos.as_view(), name='individuos'),
    path('cirueloRojo', views.CirueloRojo.as_view(), name='cirueloRojo'),
    path('olivo', views.Olivo.as_view(), name='olivo'),
    path('acebo', views.Acebo.as_view(), name='acebo'),
    path('catalpa', views.Catalpa.as_view(), name='catalpa'),
    path('pinsapo', views.Pinsapo.as_view(), name='pinsapo'),
    url(r'^registrate/$', views.SignUpView.as_view(), name='sign_up'),
    url(r'^inicia-sesion/$', views.SignInView.as_view(), name='sign_in'),
    url(r'^cerrar-sesion/$', views.SignOutView.as_view(), name='sign_out'),
    path('import', importar, name='import'),
    #path('export', some_view, name='export'),
    path('individuos/print', individuo_print, name='individuo_print'),
]
