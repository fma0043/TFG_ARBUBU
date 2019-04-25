from django.urls import include, path, re_path

from . import views

app_name="pantallaPrincipal_app"

urlpatterns = [
    path('arbol', views.ListaArboles.as_view(),name="lista-arboles"),
]
