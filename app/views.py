from django.shortcuts import render
from .forms import *
from .models import *
import os
from mysite.settings import MEDIA_ROOT
from django.http import HttpResponse
from django.views.generic import View
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
from django.http import HttpResponse

from django.utils.crypto import get_random_string


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



@csrf_exempt
def save_audio(request, *args, **kwargs):
    print(" ele post")
    if request.method == 'POST':
        print(" ele post")
        #prueba = request.FILES["file"]
        #generamos token para evitar que se sobre escriba MODIFICAR
        token = get_random_string(length=6)
        archivo = f"audio{token}.mp3"
        print("token")
        audio_file = request.body
        print(audio_file)
        #Guarda el archivo
        file = default_storage.open(archivo, 'wb')
        # Escribir el contenido del archivo
        file.write(audio_file)
        # Cerrar el archivo
        file.close()
        # Devolver la ubicación del archivo
        print(file)

        #Convertimos la url en str
        stinggg = str(file)
        print(stinggg);
        #Cortamos la url 
        urlAudio = stinggg.split("\media")
        #traemos la ubicacion del archivo
        urlAudio = urlAudio[1]
        print(urlAudio)       
        document = Media.objects.create(audio=urlAudio)
        document.save()
        #audio.grabarAudio(prueba)
        #return render(request, 'app/vocalizacion.html')
        return HttpResponse("SI")
    return render(request, 'app/vocalizacion.html')




########################## VOCALIZACION ################################
############## CONFIGURAR CORRECTAMENTE PARA GUARDAR#####################
class VocalizacionView(View):

    def get(self, request, *args, **kwargs):
        print(request.user.id)
        return render(request, 'app/vocalizacion.html')

    def post(self, request, *args, **kwargs):
        print(request)
        # audio = Audio()
        # audio.grabarAudio(str(request.user.id))
        return render(request, 'app/vocalizacion.html')
    
    # def save_audio(self, request, *args, **kwargs):
    #     if request.method == 'POST':
    #         print(" el post")
    #         audio_file = request
    #         print(audio_file)
    #     return render(request, 'app/vocalizacion.html')
    

    