from django.contrib import admin
from .models import *
# Register your models here.

# VOCALIZACION


class VocalizacionAdmin(admin.ModelAdmin):
    list_display = ["usuario", "audio"]  # , "bpm", "beats", "timestamp"


admin.site.register(Vocalizacion, VocalizacionAdmin)


# INTENSIDAD
class IntensidadAdmin(admin.ModelAdmin):
    list_display = ["usuario", "audio"]  # , "bpm", "beats", "timestamp"


admin.site.register(Intensidad, IntensidadAdmin)


# MEMORICE


class MemoriceAdmin(admin.ModelAdmin):
    list_display = ["usuario", "acierto", "tiempo",
                    "movimientos", "timestamp"]


admin.site.register(Memorice, MemoriceAdmin)

# EJERCICIO DE PALABRAS


class VocalPalabrasAdmin(admin.ModelAdmin):
    list_display = ["usuario", "audio", "timestamp"]


admin.site.register(VocalPalabras, VocalPalabrasAdmin)

# LECTURA TEXTO


class VocalTextoAdmin(admin.ModelAdmin):
    list_display = ["usuario", "audio", "timestamp"]


admin.site.register(VocalTexto, VocalTextoAdmin)
