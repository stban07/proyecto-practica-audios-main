from rest_framework import serializers
from .models import ExampleModel

from app.models import Profesional_salud

class ExampleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleModel
        fields = '__all__'


class Profesional_saludSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesional_salud
        fields = '__all__'