from django import forms

from .models import *

class CursoForm(forms.ModelForm):
    class Meta:
        
        model = Curso 
        fields = '__all__'