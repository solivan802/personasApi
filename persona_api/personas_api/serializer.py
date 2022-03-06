from rest_framework import serializers
from persona_api.models import persona
from dataclasses import fields

class persona_serializer(serializers.ModelSerializer):
    class Meta:
        model = persona
        fields = ('id','nombre','apellido','fecha','dui','telefono','direccion')
