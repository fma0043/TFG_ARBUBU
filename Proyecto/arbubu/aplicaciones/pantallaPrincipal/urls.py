from django.conf.urls import url
from django.urls import include, path, re_path


from . import views

app_name="pantallaPrincipal_app"

urlpatterns = [
    path('familia', views.ListaFamilias.as_view(),name="lista-familias"),
    path('especie', views.ListaEspecies.as_view(),name="lista-especies"),
    path('individuo', views.ListaIndividuos.as_view(),name="lista-individuo"),
    path('usuario', views.ListaUsuarios.as_view(),name="lista-usuario"),
    path('index', views.IndexView.as_view(),name="index"),
    #path('añadirIndividuo', views.AddIndividuo.as_view(), name="add-individuo"),
]
