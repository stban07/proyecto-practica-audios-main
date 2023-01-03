from django import forms
from .models import *

# VOCALIZACION O METRONOMO


class VocalizacionForm(forms.ModelForm):
    class Meta:
        """Meta definition for Vocalizacionform."""

        model = Vocalizacion
        fields = '__all__'  # 'beats', 'bpm'


# INTENSIDAD
class IntensidadForm(forms.ModelForm):
    class Meta:
        """Meta definition for Vocalizacionform."""

        model = Intensidad
        fields = '__all__'

# MEMORICE


class MemoriceForm(forms.ModelForm):
    acierto = forms.CharField(label='Cantidad de aciertos', widget=forms.TextInput(
        attrs={

            'placeholder': 'Ingresa cantidad de aciertos',
            'id': 'total_acierto'
        }))

    tiempo = forms.CharField(label='Cantidad de tiempo', widget=forms.TextInput(
        attrs={

            'placeholder': 'Ingresa cantidad de tiempo',
            'id': 'total_tiempo'
        }))

    movimientos = forms.CharField(label='Cantidad de movimientos', widget=forms.TextInput(
        attrs={

            'placeholder': 'Ingresa cantidad de movimientos',
            'id': 'total_movimientos'
        }))

    class Meta:
        model = Memorice
        fields = 'acierto', 'tiempo', 'movimientos'

# EJERCICIO PALABRAS


class VocalPalabras(forms.ModelForm):
    class Meta:
        model = VocalPalabras
        fields = '__all__'

# LECTURA DE TEXTO


class VocalTexto(forms.ModelForm):
    class Meta:
        model = VocalTexto
        fields = '__all__'
