from django.contrib import admin
from .models import *
# Register your models here.

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin



# class UsuarioAdmin(admin.ModelAdmin):
#      list_display = ("username", "email", "first_name", "last_name", "is_staff")
# admin.site.register(Usuario, UsuarioAdmin)



class UserAdmin(BaseUserAdmin): 
    list_display = ('id','username','email','first_name', 'last_name', 'id_tipo_user') 
    list_filter = ('email',) 
    fieldsets = ( 
        (None,{'fields': ('username','email', 'password')}), 
        ('Informacion personal', {'fields': ( 'first_name', 'last_name', 'id_tipo_user')}), 
        ('Permisos Django', {'fields': ('is_staff', 'is_active')}) 
 
    ) 
 
    add_fieldsets = ( 
        (None, { 
            'classes':('wide',), 
            'fields':('id_tipo_user','username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        }), 
    ) 



admin.site.register(Usuario, UserAdmin)



# #Region
class RegionAdmin(admin.ModelAdmin):
     list_display = ["id_region","nombre_region"]  # , "bpm", "beats", "timestamp"
admin.site.register(Region, RegionAdmin)


# #Provincia
class ProvinciaAdmin(admin.ModelAdmin):
     list_display = ["id_provincia","nombre_provincia","id_region"]  # , "bpm", "beats", "timestamp"
admin.site.register(Provincia, ProvinciaAdmin)


# #Comuna
class ComunaAdmin(admin.ModelAdmin):
     list_display = ["id_comuna","nombre_comuna","id_provincia"]  # , "bpm", "beats", "timestamp"
admin.site.register(Comuna, ComunaAdmin)



# #INSTITUCION
class InstitucionAdmin(admin.ModelAdmin):
     list_display = ["id_institucion","nombre_institucion","descripcion","comuna"]  # , "bpm", "beats", "timestamp"
admin.site.register(Institucion, InstitucionAdmin)



# #Fonoaudiologo
class FonoaudilogosAdmin(admin.ModelAdmin):
     list_display = ["rut","NombreCompleto","preregistrado"]  # , "bpm", "beats", "timestamp"
admin.site.register(Fonoaudilogos, FonoaudilogosAdmin)



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




# #Pre-registro
class PreRegistroAdmin(admin.ModelAdmin):
     list_display = ["rut","nombre", "apellido","tipo_user","email","telefono"] 
admin.site.register(PreRegistro, PreRegistroAdmin)






# #PROFESIONAL SALUD
class ProfesionalAdmin(admin.ModelAdmin):
     list_display = ["id_profesional","rut_profesional", "id_usuario","institucion_id"] 
admin.site.register(Profesional_salud, ProfesionalAdmin)




# #TIPOS DE USUARIO
class TipoUserAdmin(admin.ModelAdmin):
      list_display = ["id","nombre_tipo_usuario", "descripcion"] 
admin.site.register(TipoUsuario, TipoUserAdmin)



# #PROFESIONAL PACIENTE
class Profesional_PacienteAdmin(admin.ModelAdmin):
     list_display = ["id_profesional_salud","id_paciente","tipo_profesional","descripcion"] 
admin.site.register(Profesional_Paciente, Profesional_PacienteAdmin)

# #AUDIO
class AudioAdmin(admin.ModelAdmin):
     list_display = ["id_audio", "url_audio", "timestamp","idusuario"]
admin.site.register(Audio,  AudioAdmin)




# # coeficiente audio
class AudiosCoeficientesAdmin(admin.ModelAdmin):
     list_display = ["id", "idusuario", "timestamp","Intensidad","F0"]
admin.site.register(AudiosCoeficientes,  AudiosCoeficientesAdmin)










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


