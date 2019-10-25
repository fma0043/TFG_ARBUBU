from django.conf.urls import url
from django.urls import include, path, re_path
from . import views
from aplicaciones.principal.views import SignUpView, SignInView, BienvenidaView, SignOutView

app_name="principal_app"

urlpatterns = [
    path('index', views.IndexView.as_view(),name="index"),
    url(r'^$', views.BienvenidaView.as_view(), name='bienvenida'),
    url(r'^registrate/$', views.SignUpView.as_view(), name='sign_up'),
    url(r'^inicia-sesion/$', views.SignInView.as_view(), name='sign_in'),
    url(r'^cerrar-sesion/$', views.SignOutView.as_view(), name='sign_out'),
]
