from django.shortcuts import render

from rest_framework import generics
from .models import ExampleModel
from .serializers import ExampleModelSerializer, Profesional_saludSerializer, AudioSerializer

from app.models import Institucion, Profesional_salud, TipoUsuario, Usuario, Audio

# Create your views here.

class ExampleModelList(generics.ListCreateAPIView):
    queryset = ExampleModel.objects.all()
    serializer_class = ExampleModelSerializer

class ExampleModelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExampleModel.objects.all()
    serializer_class = ExampleModelSerializer

class Profesional_saludList(generics.ListCreateAPIView):
    serializer_class = Profesional_saludSerializer

    def get_queryset(self):
        institucion_id = self.request.query_params.get('institucion_id')
        nombre_institucion = self.request.query_params.get('nombre_institucion')
        id_usuario = self.request.query_params.get('id_usuario')
        # id_tipo_user = self.request.query_params.get('nombre_tipo_usuario')
        queryset = Profesional_salud.objects.all()
        if id_usuario and institucion_id:
            queryset = queryset.filter(institucion_id=institucion_id).filter(id_usuario=id_usuario)

        elif nombre_institucion:
            institucion_id = Institucion.objects.get(nombre_institucion=nombre_institucion).id_institucion
            queryset = queryset.filter(institucion_id=institucion_id)

        elif institucion_id:
            queryset = queryset.filter(institucion_id=institucion_id)

        # elif nombre_tipo_usuario:
        #     nombre_tipo_usuario = Usuario.objects.get(id_tipo_user=id_tipo_user).id_tipo_user.nombre_tipo_usuario
        #     queryset = queryset.filter(id_usuario=id_usuario)

        elif id_usuario:
            queryset = queryset.filter(id_usuario=id_usuario)

        return queryset

class AudioList(generics.ListCreateAPIView):
    serializer_class = AudioSerializer

    def get_queryset(self):
        idusuario = self.request.query_params.get('institucion_id')
        url_audio = self.request.query_params.get('url_audio')
        queryset = Audio.objects.all()
        

        if url_audio:
            queryset = queryset.filter(url_audio__endswith=url_audio)

        return queryset