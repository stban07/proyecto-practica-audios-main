from django.shortcuts import render
from .forms import *
from .models import *
import os
from mysite.settings import MEDIA_ROOT
from django.http import HttpResponse
from audio.audio import Audio
from django.views.generic import View
from django.http import JsonResponse
from django.shortcuts import redirect

############### INDEX #####################


def index(request):
    return render(request, 'app/index.html')

############### INTENSIDAD #####################


class IntensidadView(View):

    def get(self, request, *args, **kwargs):
        print(request.user.id)
        return render(request, 'app/intensidad.html')

    def post(self, request, *args, **kwargs):
        print("hola estoy en el post")
        audio = Audio()
        audio.grabarAudio(str(request.user.id))
        return render(request, 'app/intensidad.html')


############### MEDIDOR DECIBEL #####################


def medidor(request):
    return render(request, 'app/medidor-sonido.html')

############### oscilograma ####################


############### EJERCICIO PALABRAS#####################


def eva_param_func(request):
    def get(self, request, *args, **kwargs):
        print(request.user.id)
        return render(request, 'app/eva_param_func.html')

    def post(self, request, *args, **kwargs):
        print("hola estoy en el post")
        audio = Audio()
        audio.grabarAudio(str(request.user.id))
    return render(request, 'app/eva_param_func.html')

################## EJERCICIO LECTURA#######################


def eva_param_text(request):
    return render(request, 'app/eva_param_text.html')

################## CRUCIGRAMA########################


def crucigrama(request):
    return render(request, 'app/crucigrama.html')

###################### MEMORICE #######################


def memorama(request):
    data = {
        'form': MemoriceForm,
    }
    if request.method == 'POST':
        formulario = MemoriceForm(data=request.POST)
        if formulario.is_valid():
            post = formulario.save(commit=False)
            post.acierto = request.POST["acierto"]
            post.tiempo = request.POST["tiempo"]
            post.movimientos = request.POST["movimientos"]
            post.usuario_id = request.user.id
            formulario.save()
        else:
            formulario = MemoriceForm()
    return render(request, 'app/memorama.html', data)
    # return render(request, 'app/memorama.html')


########################## VOCALIZACION ################################
############## CONFIGURAR CORRECTAMENTE PARA GUARDAR#####################
class VocalizacionView(View):

    def get(self, request, *args, **kwargs):
        print(request.user.id)
        return render(request, 'app/vocalizacion.html')

    def post(self, request, *args, **kwargs):
        print("hola estoy en el post")
        audio = Audio()
        audio.grabarAudio(str(request.user.id))
        return render(request, 'app/vocalizacion.html')
