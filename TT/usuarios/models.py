from django.db import models


class Persona(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, auto_created=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=10)
    correo = models.EmailField()

    class Meta:
        ordering = ['id']
        indexes = [models.Index(fields=['id']), ]


class Alumno(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, auto_created=True)
    num_boleta = models.CharField(unique=True, max_length=255)
    carrera = models.CharField(max_length=50)
    plan = models.CharField(max_length=50)
    nombre_protocolo = models.CharField(max_length=50)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

    class Meta:
        ordering = ['num_boleta']
        indexes = [models.Index(fields=['num_boleta']), ]

