from django.shortcuts import render

from rest_framework import generics
from .models import ExampleModel
from .serializers import ExampleModelSerializer, Profesional_saludSerializer

from app.models import Profesional_salud

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
        id_usuario = self.request.query_params.get('id_usuario')
        queryset = Profesional_salud.objects.all()
        if id_usuario and institucion_id:
            queryset = queryset.filter(institucion_id=institucion_id).filter(id_usuario=id_usuario)

        elif institucion_id:
            queryset = queryset.filter(institucion_id=institucion_id)

        elif id_usuario:
            queryset = queryset.filter(id_usuario=id_usuario)

        return queryset