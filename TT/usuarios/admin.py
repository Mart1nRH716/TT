from django.contrib import admin

from usuarios.models import Alumno, Profesor

# Register your models here.
# admin.site.register(Post) #Aqui hay quye registar todos nuetsros modelos para que django pueda encontrarlos


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ['num_boleta', 'carrera', 'plan']  # Define qué campos del modelo Persona se mostrarán en la lista de elementos del panel de administración
    list_filter = ['num_boleta', 'carrera', 'plan'] # Agregar filtros en el panel de administracion
    search_fields = ['num_boleta', 'carrera', 'plan'] # Define los campos que se utilizan para la busqueda
    ordering = ['num_boleta', 'carrera']  # define el orden en el que se mostrarán los elementos en el panel de administración

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ['matricula', 'materias', 'user']
    list_filter = ['matricula', 'materias', 'user']
    search_fields = ['matricula', 'materias', 'user']
    ordering = ['matricula']