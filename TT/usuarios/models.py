from django.db import models


class Persona(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, auto_created=True)
    nombre = models.CharField(max_length=20)
    appellido = models.CharField(max_length=20)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=10)
    correo = models.EmailField()

    class Meta:
        ordering = ['id']
        indexes = [models.Index(fields=['id']), ]


class Alumno(models.Model):
    num_boleta = models.CharField(primary_key=True, unique=True, max_length=256)
    carrera = models.CharField(max_length=50)
    nombre_protocolo = models.CharField(max_length=50)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=10)
    correo = models.EmailField()
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

    class Meta:
        ordering = ['num_boleta']
        indexes = [models.Index(fields=['num_boleta']), ]

