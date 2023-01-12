from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
# Create your models here.

# VOCALIZACION O METRONOMO
class Media(models.Model):
    audio = models.FileField(upload_to='media')
    timestamp = models.CharField(max_length=100)
    ###FOREIGNKEYS  
    idPaciente = models.CharField(max_length=100)
    # idIntensidad = models.CharField(max_length=100)
    def __str__(self):
        return str(self.audio)

# INTENSIDAD
class Intensidad(models.Model):
    idusuario = models.BigAutoField(primary_key=True)
    bpm = models.CharField(max_length=100)
    tiempo = models.CharField(max_length=100)
    def __str__(self):
        return str(self.tiempo)



#PACIENTE
class Paciente(models.Model):
    idPaciente = models.BigAutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Edad = models.CharField(max_length=100)
    Sexo = models.CharField(max_length=100)
    Observacion = models.CharField(max_length=100)
    def __str__(self):
        return str(self.Nombre)















# # MEMORICE O MEMORAMA


# class Memorice(models.Model):
#     acierto = models.CharField(max_length=200)
#     tiempo = models.CharField(max_length=100)
#     movimientos = models.CharField(max_length=100)
#     usuario = models.ForeignKey(User, on_delete=models.CASCADE)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return str(self.usuario)

# # EJERCICIO PALABRAS


# class VocalPalabras(models.Model):
#     usuario = models.ForeignKey(User, on_delete=models.CASCADE)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     audio = models.FileField(upload_to='archivos_media')

#     def __str__(self):
#         return str(self.usuario)

# # EJERCICIO LECTURA


# class VocalTexto(models.Model):
#     usuario = models.ForeignKey(User, on_delete=models.CASCADE)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     audio = models.FileField(upload_to='archivos_media')

#     def __str__(self):
#         return str(self.usuario)
