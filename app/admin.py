from django.contrib import admin
from .models import *
# Register your models here.

# VOCALIZACION

class MediaAdmin(admin.ModelAdmin):
    list_display = ["audio","timestamp","idPaciente",]  # , "bpm", "beats", "timestamp"
admin.site.register(Media, MediaAdmin)




# INTENSIDAD
class IntensidadAdmin(admin.ModelAdmin):
    list_display = ["idusuario","bpm", "tiempo"]  # , "bpm", "beats", "timestamp"
admin.site.register(Intensidad, IntensidadAdmin)




class PacienteAdmin(admin.ModelAdmin):
        list_display = ["idPaciente","Nombre", "Apellido","Edad","Sexo","Observacion"]  # , "bpm", "beats", "timestamp"
admin.site.register(Paciente, PacienteAdmin)














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


# class VocalTextoAdmin(admin.ModelAdmin):
#     list_display = ["usuario", "audio", "timestamp"]


# admin.site.register(VocalTexto, VocalTextoAdmin)
