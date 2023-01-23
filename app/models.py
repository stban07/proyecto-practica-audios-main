from __future__ import unicode_literals 
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here. 
##FALTA CREAR TABLAS DE 
###PROVINCIA-REGION(se relacionan con comuna) Y 6 TABLAS DE PACIENTE

#TipoUsuario
class TipoUsuario(models.Model):
        nombre_tipo_usuario = models.CharField(max_length=100)
        descripcion = models.CharField(max_length=100)
        def __str__(self):
            return str(self.nombre_tipo_usuario)

# # #COMUNA
class Comuna(models.Model):
       id_comuna = models.BigAutoField(primary_key=True)
       nombre_comuna = models.CharField(max_length=100)
       def __str__(self):
           return str(self.nombre_comuna)
    
# # #Institucion
class Institucion(models.Model):
       id_institucion = models.BigAutoField(primary_key=True)
       nombre_institucion = models.CharField(max_length=100)
       descripcion = models.CharField(max_length=100)
       comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE,null=True)
       def __str__(self):
           return str(self.nombre_institucion)    
    


# # # #USUARIO
class Usuario(AbstractUser):
       # username = models.CharField(unique=True, max_length=150)
       # password = models.CharField(max_length=128)
       id_tipo_user = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE,null=True)
       comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE,null=True)



# # # # #PACIENTE
class Paciente(models.Model):
       idPaciente = models.BigAutoField(primary_key=True)
       rut_paciente = models.CharField(max_length=100)
       telegram_paciente = models.CharField(max_length=100)
       diabetes = models.CharField(max_length=100)
       hipertencion = models.CharField(max_length=100)
       Observacion = models.CharField(max_length=100)
       id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE,null=True)
       def __str__(self):
           return str(self.rut_paciente)
    
# #FAMILIAR
class Familiar(models.Model):
     id_familiar = models.BigAutoField(primary_key=True)
     rut_familiar = models.CharField(max_length=100)
     id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE,null=True)
     def __str__(self):
         return str(self.rut_familiar)
  
  
  
# #FAMILIAR_PACIENTE
class Familiar_paciente(models.Model):
     id_fam_pac = models.BigAutoField(primary_key=True)
     id_familiar = models.ForeignKey(Familiar, on_delete=models.CASCADE,null=True)
     id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE,null=True)
     parentesco  = models.CharField(max_length=100)
     def __str__(self):
         return str(self.parentesco)  
    
    
# #PROFESIONAL SALUD
class Profesional_salud(models.Model):
     id_profesional = models.BigAutoField(primary_key=True)
     rut_profesional = models.CharField(max_length=100)
     id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE,null=True)
     institucion_id = models.ForeignKey(Institucion, on_delete=models.CASCADE,null=True)
     def __str__(self):
         return str(self.rut_profesional)




# #PROFESIONAL PACIENTE
class Profesional_Paciente(models.Model):
     id_prof_paci = models.BigAutoField(primary_key=True)
     descripcion = models.CharField(max_length=100)
     id_profesional_salud = models.ForeignKey(Profesional_salud, on_delete=models.CASCADE,null=True)
     id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE,null=True)
     def __str__(self):
         return str(self.descripcion)




# # AUDIO
class Audio(models.Model):
     id_audio = models.BigAutoField(primary_key=True)
     url_audio = models.FileField(upload_to='media')
     timestamp = models.CharField(max_length=100)
     idusuario = models.ForeignKey(Usuario, on_delete=models.CASCADE,null=True)
     def __str__(self):
         return str(self.url_audio)




# # PARAMETRO
class Parametros(models.Model):
     tiempoVocalizacion = models.CharField(max_length=100)
     tiempoIntensidad = models.CharField(max_length=100)
     Descripcion = models.CharField(max_length=100)
     def __str__(self):
         return str(self.tiempoVocalizacion)

















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



#class AppMedia(models.Model):
#    id = models.BigAutoField(primary_key=True)
#    audio = models.CharField(max_length=100)
#    timestamp = models.CharField(max_length=100)
#    idpaciente = models.CharField(db_column='idPaciente', max_length=100)  # Field name made lowercase.       
#
#    class Meta:
#        managed = False
#        db_table = 'app_media'






