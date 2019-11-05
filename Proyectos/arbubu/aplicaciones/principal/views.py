from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse

from django.template import RequestContext

from django.views.generic import ListView, TemplateView, CreateView

from django.contrib import auth

from .models import Usuario, Familia, Genero

from .forms import SignUpForm

from django.contrib.auth.views import LoginView, LogoutView

class IndexView(TemplateView):

    template_name = "principal/index.html"

class Familias(ListView):

    template_name = "principal/familias.html"
    model = Familia
    context_object_name = 'familia'

class Generos(ListView):

    template_name = "principal/generos.html"
    model = Genero
    context_object_name = 'genero'

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
