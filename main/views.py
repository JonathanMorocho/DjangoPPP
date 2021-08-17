from main.forms import CursoForm
import main
from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.db.models import Sum
from inscripciones.models import*
from .models import Curso
  
# Create your views here.

def homepage(request):
    return render(request, "main/inicio.html", {"cursos": Curso.objects.all})

def registro(request):

    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            nombre_usuario = form.cleaned_data.get('username')
            messages.success(request, f"Nueva Cuenta Creada : {nombre_usuario}")
            login(request, usuario)
            messages.info(request, f"Has sido logeado")
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

    form = UserCreationForm 
    return render(request, "main/registro.html", {"form":form})


def logout_request(request):
    logout(request)
    messages.info(request, "Saliste exitosamente")
    return redirect("main:homepage")

def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            user = authenticate(username = usuario, password = contraseña)

            if user is not None:
                login(request, user)
                messages.info(request, f"Estas logeado como {usuario}")
                return redirect("main:homepage")
            else:
                messages.info(request, f"Usuario o contraseña incorrecta")
        else:
            messages.info(request, f"Usuario o contraseña incorrecta")

    form = AuthenticationForm()
    return render(request, "main/login.html", {"form": form})

def crear_curso(request):
    form = CursoForm() 
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:lista_form')
        else: 
            context = {
                'forms': form
            }
            return redirect(request, "main/curso_forms.html", context)
    context = {
        'forms': form
    }
    return render(request, "main/curso_forms.html", context)


def lista_form(request):
    cursos = Curso.objects.all()
    context = {
        'cursos':cursos
    }
    return render(request, "main/listas.html", context)


def eliminarCurso(request,id):
    curso = Curso.objects.get(id = id)
    curso.delete()
    return redirect('main:lista_form')


def editarCurso(request,id):
    curso = Curso.objects.get(id = id)
    print(curso)
    form = CursoForm(instance = curso)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance= curso)
        if form.is_valid():
            form.save()
            messages.info(request, f"Curso editado correctamente")
            return redirect('main:lista_form')
    contexto = {
            'form': form
        }
    return render(request, "main/agregar.html", contexto)


def inscritosCurso(request, id):
    cursos = Curso.objects.get(id=id)
    inscritos_curso = Inscripcion.objects.filter(curso = cursos)
    suma_costos = inscritos_curso.aggregate(Sum('costo_total'))
    contexto = {
        'cursos': cursos,
        'inscritos_curso': inscritos_curso, 
        'suma_costos': suma_costos  
    }
    return render(request, 'inscripciones/lista_inscritos.html', contexto)