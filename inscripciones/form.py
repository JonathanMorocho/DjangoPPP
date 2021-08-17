from django import forms
from django.contrib.auth.models import User
from django.db.models import fields
from django.forms.fields import CharField
from  .models import Inscripcion
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username'
        ]
        labels = {
            'username': 'Nombre de usuario',
            

        }

class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
    
        fields = ('Nombres',
                    'Apellidos',
                    'edad',
                    'fecha_inscripcion',
                    'costo_total')

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]
        labels = {
            'username' : 'Nombre de usuario',
            'email': 'Correo Electronico',

        }
class CursoForm(forms.ModelForm):
    class Meta:
        
        model = Inscripcion 
        fields = '__all__'
