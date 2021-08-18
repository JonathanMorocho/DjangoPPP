from django.db.models.aggregates import Count
from inscripciones.form import EstudianteForm, InscripcionForm, RegistroForm
from main.views import registro
from sys import prefix
from .models import Inscripcion
from django.shortcuts import redirect, render
from django.contrib import messages
from main.models import Curso
from django.db.models import Sum



# Create your views here.
#Para guardar las inscripciones
def inscripciones_form(request, pk):
    print('Registro de Inscripciones')
    registro_form = RegistroForm(prefix='form_registro')
    inscripcion_form = InscripcionForm(prefix='form inscripcion')

    contexto = {
        'registro_form' : registro_form,
        'inscripcion_form' : inscripcion_form
    }
    if request.method == 'POST':
        registro_form = RegistroForm(request.POST, prefix='form_registro')
        inscripcion_form = InscripcionForm(request.POST, prefix='form inscripcion')

        if registro_form.is_valid() and inscripcion_form.is_valid():
            estudiante = registro_form.save(commit=False)
            print('giuardo aki1')
            estudiante.user = request.user
            estudiante.save()
            curso = Curso.objects.get(pk = pk)
            print('2')
            inscripcion = inscripcion_form.save(commit=False)
            inscripcion.curso = curso
            inscripcion.estudiante = estudiante
            inscripcion.save()
            return redirect('inscripciones:lista_estudiantes')
        else: 
            print('ERRORR')
            print(inscripcion_form.errors)
            messages.error(request, registro_form.errors)
            messages.error(request, inscripcion_form.errors)
    return render(request, 'inscripciones/inscripcion_form.html', contexto)


#para mostrar la lista de inscripciones
def lista_estudiantes(request):
    
    return render(request, "inscripciones/lista_inscritos.html", {"inscritos_curso":Inscripcion.objects.all})

#eliminar estudiantes
def eliminar_inscripcion(request,id):
    inscripcion = Inscripcion.objects.get(id = id)
    inscripcion.delete()
    return redirect('inscripciones:lista_estudiantes')  

#editar estudiantes 
def editar_inscripcion(request, id):
    inscripcion = Inscripcion.objects.get(id = id)
    user = inscripcion.estudiante
    if request.method == 'GET':
        estudiante_form = EstudianteForm(instance=user)
        inscripcion_form = InscripcionForm(instance=inscripcion) 
        contexto = {
        'estudiante_form':estudiante_form,
        'inscripcion_form':inscripcion_form

        }
    else:
        estudiante_form = EstudianteForm(request.POST, instance=user)
        inscripcion_form = InscripcionForm(request.POST, instance=inscripcion) 
        contexto = {
        'estudiante_form':estudiante_form,
        'inscripcion_form':inscripcion_form

        }
        if estudiante_form.is_valid() and inscripcion_form.is_valid():
            estudiante = estudiante_form.save(commit=False)
            estudiante.user = request.user
            estudiante.save()
            
            inscripcion = inscripcion_form.save(commit=False)
            inscripcion.estudiante = estudiante
            inscripcion.save()
            return redirect('inscripciones:lista_estudiantes')

        else:
            print('Error en los forms')
            print(inscripcion_form.errors)
            messages.error(request, estudiante_form.errors)
            messages.error(request, inscripcion_form.errors)
    return render(request,'inscripciones/editar_form.html', contexto)



def edadPromedio(request, id):
    cursos = Curso.objects.get(id=id)
    inscritos_curso = Inscripcion.objects.filter(curso = cursos)
    suma_costos = inscritos_curso.aggregate(Sum('edad'))
    print(suma_costos)
    tamaño = inscritos_curso.aggregate(Count('edad'))
    print(tamaño)
    contexto = {
        'cursos': cursos,
        'inscritos_curso': inscritos_curso, 
        'suma_costos': suma_costos,
        'tamaño' : tamaño,
    }
    return render(request, 'inscripciones/lista_inscritos.html', contexto)


