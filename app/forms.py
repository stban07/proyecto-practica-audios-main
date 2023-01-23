from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

User = Usuario;


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields











# class MemoriceForm(forms.ModelForm):
#     acierto = forms.CharField(label='Cantidad de aciertos', widget=forms.TextInput(
#         attrs={

#             'placeholder': 'Ingresa cantidad de aciertos',
#             'id': 'total_acierto'
#         }))

#     tiempo = forms.CharField(label='Cantidad de tiempo', widget=forms.TextInput(
#         attrs={

#             'placeholder': 'Ingresa cantidad de tiempo',
#             'id': 'total_tiempo'
#         }))

#     movimientos = forms.CharField(label='Cantidad de movimientos', widget=forms.TextInput(
#         attrs={

#             'placeholder': 'Ingresa cantidad de movimientos',
#             'id': 'total_movimientos'
#         }))

#     class Meta:
#         model = Memorice
#         fields = 'acierto', 'tiempo', 'movimientos'

# # EJERCICIO PALABRAS


# class VocalPalabras(forms.ModelForm):
#     class Meta:
#         model = VocalPalabras
#         fields = '__all__'

# # LECTURA DE TEXTO


# class VocalTexto(forms.ModelForm):
#     class Meta:
#         model = VocalTexto
#         fields = '__all__'
