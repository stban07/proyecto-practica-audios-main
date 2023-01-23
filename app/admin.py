from django.contrib import admin
from .models import *
# Register your models here.





class UsuarioAdmin(admin.ModelAdmin):
     list_display = ("username", "email", "first_name", "last_name", "is_staff")
admin.site.register(Usuario, UsuarioAdmin)

# #Comuna
class ComunaAdmin(admin.ModelAdmin):
     list_display = ["id_comuna","nombre_comuna"]  # , "bpm", "beats", "timestamp"
admin.site.register(Comuna, ComunaAdmin)



# #INSTITUCION
class InstitucionAdmin(admin.ModelAdmin):
     list_display = ["id_institucion","nombre_institucion","descripcion","comuna"]  # , "bpm", "beats", "timestamp"
admin.site.register(Institucion, InstitucionAdmin)




# # PARAMETRO
class ParametroAdmin(admin.ModelAdmin):
     list_display = ["tiempoVocalizacion", "tiempoIntensidad", "Descripcion"]  # , "bpm", "beats", "timestamp"
admin.site.register(Parametros, ParametroAdmin)


# #PACIENTE
class PacienteAdmin(admin.ModelAdmin):
    list_display = ["idPaciente","rut_paciente", "telegram_paciente","diabetes","hipertencion","Observacion","id_usuario"]  # , "bpm", "beats", "timestamp"
admin.site.register(Paciente, PacienteAdmin)




# #FAMILIA
class FamiliarAdmin(admin.ModelAdmin):
     list_display = ["id_familiar","rut_familiar", "id_usuario"] 
admin.site.register(Familiar, FamiliarAdmin)



# #FAMILIAR PACIENTE
class Familiar_pacienteAdmin(admin.ModelAdmin):
     list_display = ["id_fam_pac","id_familiar", "id_paciente","parentesco"] 
admin.site.register(Familiar_paciente, Familiar_pacienteAdmin)






# #PROFESIONAL SALUD
class ProfesionalAdmin(admin.ModelAdmin):
     list_display = ["id_profesional","rut_profesional", "id_usuario","institucion_id"] 
admin.site.register(Profesional_salud, ProfesionalAdmin)




# #TIPOS DE USUARIO
class TipoUserAdmin(admin.ModelAdmin):
      list_display = ["nombre_tipo_usuario", "descripcion"] 
admin.site.register(TipoUsuario, TipoUserAdmin)



# #PROFESIONAL PACIENTE
class Profesional_PacienteAdmin(admin.ModelAdmin):
     list_display = ["id_prof_paci","descripcion", "id_profesional_salud","id_paciente"] 
admin.site.register(Profesional_Paciente, Profesional_PacienteAdmin)

# #AUDIO
class AudioAdmin(admin.ModelAdmin):
     list_display = ["id_audio", "url_audio", "timestamp","idusuario"]
admin.site.register(Audio,  AudioAdmin)















# # MEMORICE


# class MemoriceAdmin(admin.ModelAdmin):
#     list_display = ["usuario", "acierto", "tiempo",
#                     "movimientos", "timestamp"]


# admin.site.register(Memorice, MemoriceAdmin)

# # EJERCICIO DE PALABRAS


# class VocalPalabrasAdmin(admin.ModelAdmin):
#     list_display = ["usuario", "audio", "timestamp"]


# admin.site.register(VocalPalabras, VocalPalabrasAdmin)

# # LECTURA TEXTO


