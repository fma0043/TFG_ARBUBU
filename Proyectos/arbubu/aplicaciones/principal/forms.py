from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Usuario, Individuos

class SignUpForm(UserCreationForm):
    nombre = forms.CharField(max_length=140, required=True)
    apellido = forms.CharField(max_length=140, required=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username','email','nombre','apellido','password1','password2','is_active','groups')

class IndividuosForm(ModelForm):

    class Meta:
        model = Individuos
        fields = ('nombreComun','especie','motivoSingular','explicacionMotivoSingular','latitud','longitud','fotoArbol','fotoHojas','fotoFrutos','ubicacion')
