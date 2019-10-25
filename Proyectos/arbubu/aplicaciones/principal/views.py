from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse

from django.template import RequestContext

from django.views.generic import ListView, TemplateView, CreateView 

from django.contrib import auth

from .models import Usuario

from .forms import SignUpForm

from django.contrib.auth.views import LoginView, LogoutView

class IndexView(TemplateView):

    template_name = "principal/index.html"


class SignUpView(CreateView):
    model = Usuario
    form_class = SignUpForm

    def form_valid(self, form):
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/')

class BienvenidaView(TemplateView):
   template_name = 'principal/bienvenida.html'

class SignInView(LoginView):
    template_name = 'principal/iniciar_sesion.html'

class SignOutView(LogoutView):
    pass
