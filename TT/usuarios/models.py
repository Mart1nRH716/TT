from django.db import models
from django.conf import settings

"""
Estaba viendo que la clase auth.user que viene con django implemneta casi todos estos campos
Lo unico que faltaria el telefono y edad, pero creo que no es relevante, por lo tanto, creo que podemos
extender el modelo de auth.user para cada modelo de Alumno y profesor 
"""
# class Persona(models.Model):
#     nombre = models.CharField(max_length=20)
#     apellido = models.CharField(max_length=20)
#     edad = models.IntegerField()
#     telefono = models.CharField(max_length=10)
#     correo = models.EmailField()
#
#     class Meta:
#         ordering = ['id']
#         indexes = [models.Index(fields=['id']), ]


class Alumno(models.Model):
    class Carrera(models.TextChoices):
        # Agregamos la clase para las carreras
        # El valor que se almacena es ISC o LCD y para no confundirlo, para nosotros se mostrara como sistemas_computacionales
        SISTEMAS = 'ISC', 'sistemas_computacionales'
        LICDATOS = 'LCD', 'licencia_datos'
        IA = 'IIA', 'inteligencia_artificial'

    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE) #Con esto agregamos campos al user por default que da Django
    num_boleta = models.CharField(unique=True, max_length=255)
    carrera = models.CharField(max_length=3, choices=Carrera.choices, default=Carrera.SISTEMAS)
    plan = models.CharField(max_length=50)
    nombre_protocolo = models.CharField(max_length=50)
    es_alumno = models.BooleanField(default=True)

    class Meta:
        ordering = ['num_boleta']
        indexes = [models.Index(fields=['num_boleta']), ]

class Profesor(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE) #Con esto agregamos campos al user por default que da Django
    matricula = models.CharField(unique=True, max_length=255)
    materias = models.CharField(max_length=255)
    es_profesor = models.BooleanField(default=True)

    class Meta:
        ordering = ['matricula']
        indexes = [models.Index(fields=['matricula']), ]

