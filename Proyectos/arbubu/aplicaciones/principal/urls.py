from django.conf.urls import url
from django.urls import include, path, re_path
from . import views
from aplicaciones.principal.views import SignUpView, SignInView, SignOutView

app_name="principal_app"

urlpatterns = [
    path('index', views.IndexView.as_view(),name='index'),
    path('familias', views.Familias.as_view(),name='familias'),
    path('generos', views.Generos.as_view(),name='generos'),
    path('especies', views.Especies.as_view(),name='especies'),
    path('individuos', views.Individuos.as_view(), name="individuos"),
    url(r'^registrate/$', views.SignUpView.as_view(), name='sign_up'),
    url(r'^inicia-sesion/$', views.SignInView.as_view(), name='sign_in'),
    url(r'^cerrar-sesion/$', views.SignOutView.as_view(), name='sign_out'),
]
