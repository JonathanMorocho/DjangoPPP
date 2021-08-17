from django.contrib import admin
from .models import Inscripcion

# Register your models here.
class InscripcionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'estudiante', 
        'fecha_inscripcion',
        'curso',
        'costo_total',
        )

    

admin.site.register(Inscripcion, InscripcionAdmin)