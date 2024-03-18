from django.db import models
from django.contrib.auth.models import AbstractUser

class Persona(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=10)
    correo = models.EmailField()

    class Meta:
        ordering = ['id']
        indexes = [models.Index(fields=['id']), ]


class Alumno(models.Model):
    class Carrera(models.TextChoices):
        # Agregamos la clase para las carreras
        # El valor que se almacena es ISC o LCD y para no confundirlo, para nosotros se mostrara como sistemas_computacionales
        SISTEMAS = 'ISC', 'sistemas_computacionales'
        LICDATOS = 'LCD', 'licencia_datos'
        IA = 'IIA', 'inteligencia_artificial'

    num_boleta = models.CharField(unique=True, max_length=255)
    carrera = models.CharField(max_length=3, choices=Carrera.choices, default=Carrera.SISTEMAS)
    plan = models.CharField(max_length=50)
    nombre_protocolo = models.CharField(max_length=50)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)


    # Campo de contraseña
    password = models.CharField(max_length=128)


    class Meta:
        ordering = ['num_boleta']
        indexes = [models.Index(fields=['num_boleta']), ]

