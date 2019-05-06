from django.urls import include, path, re_path

from . import views

app_name="pantallaPrincipal_app"

urlpatterns = [
    path('', views.ListaArboles.as_view(),name="lista-familias"),
    path('especie/<pk>', views.ListaEspecies.as_view(),name="lista-especies"),
    path('individuo', views.ListaIndividuos.as_view(),name="lista-individuo"),
    #path('añadirIndividuo', views.AddIndividuo.as_view(), name="add-individuo"),
]
