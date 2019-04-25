from django.contrib import admin
from django.urls import path, re_path, include
##re_path(r'^', include('aplicaciones.pantallaPrincipal.urls')),
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include('aplicaciones.home.urls')),
]
