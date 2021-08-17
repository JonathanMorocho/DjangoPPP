from django.urls import path, include
from . import views

urlpatterns = [
    path('inscripciones_form/<int:pk>/', views.inscripciones_form, name='inscripciones_form'),
    path('lista_estudiantes/', views.lista_estudiantes, name='lista_estudiantes'),
    path('eliminar_inscripcion/<int:id>/', views.eliminar_inscripcion, name= 'eliminar_inscripcion'),
    path('editar_inscripcion/<int:id>/', views.editar_inscripcion, name= 'editar_inscripcion'),
]   
