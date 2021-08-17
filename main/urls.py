from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('registro/', views.registro, name="registro"),
    path('logout/', views.logout_request, name="logout"),
    path('login/', views.login_request, name='login'),
    path('crear_curso/', views.crear_curso, name='crear_curso'),
    path('eliminarCurso/<int:id>/', views.eliminarCurso, name= 'eliminarCurso'),
    path('editarCurso/<int:id>/', views.editarCurso, name='editarCurso'),
    path('lista_form/', views.lista_form, name='lista_form'),
    path('inscritos_curso/<int:id>/', views.inscritosCurso, name="inscritos_curso"),

]