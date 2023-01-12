from django.shortcuts import render
from .forms import *
from .models import *
from django.http import HttpResponse
from django.views.generic import View

from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage

from django.http import HttpResponse,JsonResponse
from django.core import serializers
from django.utils.crypto import get_random_string
from datetime import datetime
import json


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
        return render(request, 'app/intensidad.html')


# ############### MEDIDOR DECIBEL #####################


# def medidor(request):
#     return render(request, 'app/medidor-sonido.html')

# ############### oscilograma ####################


# ############### EJERCICIO PALABRAS#####################


# def eva_param_func(request):
#     def get(self, request, *args, **kwargs):
#         print(request.user.id)
#         return render(request, 'app/eva_param_func.html')

#     def post(self, request, *args, **kwargs):
#         print("hola estoy en el post")
#     return render(request, 'app/eva_param_func.html')

# ################## EJERCICIO LECTURA#######################


# def eva_param_text(request):
#     return render(request, 'app/eva_param_text.html')

# ################## CRUCIGRAMA########################


# def crucigrama(request):
#     return render(request, 'app/crucigrama.html')

# ###################### MEMORICE #######################


# def memorama(request):
#     data = {
#         'form': MemoriceForm,
#     }
#     if request.method == 'POST':
#         formulario = MemoriceForm(data=request.POST)
#         if formulario.is_valid():
#             post = formulario.save(commit=False)
#             post.acierto = request.POST["acierto"]
#             post.tiempo = request.POST["tiempo"]
#             post.movimientos = request.POST["movimientos"]
#             post.usuario_id = request.user.id
#             formulario.save()
#         else:
#             formulario = MemoriceForm()
#     return render(request, 'app/memorama.html', data)
#     # return render(request, 'app/memorama.html')



@csrf_exempt
def save_audio(request, *args, **kwargs):

    if request.method == 'POST':
        #generamos token para evitar que se sobre escriba MODIFICAR
        now = datetime.now()
        current_time = now.strftime("%d-%m-%Y %H:%M.%S")
        hms = now.strftime("%H:%M.%S")
        token = get_random_string(length=2)
        archivo = f"{token}_{hms}_vocal.mp3"
        audio_file = request.body
        #Guarda el archivo
        file = default_storage.open(archivo, 'wb')
        # Escribir el contenido del archivo
        file.write(audio_file)
        # Cerrar el archivo # Devolver la ubicación del archivo
        file.close()

        #ELIMINAR ESTE CODIGO EN PYTHONANYWHERE######
        #Convertimos la url en str
        stinggg = str(file)
        #Cortamos la url
        urlAudio = stinggg.split("\media")
        #traemos la ubicacion del archivo
        urlAudio = urlAudio[1]
        #############################################

        document = Media.objects.create(audio=urlAudio,timestamp=current_time)
        document.save()
        #audio.grabarAudio(prueba)
        #return render(request, 'app/vocalizacion.html')
        return HttpResponse("200")

    if request.method == 'GET':
        obj = str(Intensidad.objects.get(idusuario=1))
        return JsonResponse({"segundos":obj})



    return render(request, 'app/vocalizacion.html')

########################## VOCALIZACION ################################
############## CONFIGURAR CORRECTAMENTE PARA GUARDAR#####################
class VocalizacionView(View):

    def get(self, request):
        obj = str(Intensidad.objects.get(idusuario=2))
        return render(request, 'app/vocalizacion.html',{"segundos":obj})
    
    def post(self, request):
        return render(request, 'app/vocalizacion.html')


