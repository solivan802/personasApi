from rest_framework import serializers
from personaApi.models import persona
from dataclasses import fields

class persona_serializer(serializers.ModelSerializer):
    class Meta:
        model = persona
        fields = ('nombre','apellido','fecha','dui','telefono','direccion')
