from django.conf.urls import url
from django.urls import include, path, re_path
from . import views

app_name="principal_app"

urlpatterns = [
    path('index', views.IndexView.as_view(),name="index"),
]
