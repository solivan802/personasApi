from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from personaApi.models import persona
from personaApi.serializer import persona_serializer

# Create your views here.

class persona_view(APIView):
    def post(self,request):
        serializer = persona_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje" : "persona se guardo"}, status = status.HTTP_201_CREATED)
        else:
            return Response({"mensaje" : "Error"}, status = status.HTTP_400_BAD_REQUEST)

    def get(self,request,id=None):
        if id:
            person = persona.objects.get(id=id)
            serializer = persona_serializer(person)
            return Response({"mensaje" : "persona econtrada", "persona" : serializer.data}, status = status.HTTP_200_OK)
        else:
            person = persona.objects.all()
            serializer = persona_serializer(person, many=True)
            return Response({"mensaje" : "persona econtrada", "persona" : serializer.data}, status = status.HTTP_200_OK)

    def put(self,request,id):
        person = persona.objects.get(id=id)
        serializer = persona_serializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje" : "persona se guardo"}, status = status.HTTP_201_CREATED)
        else:
            return Response({"mensaje" : "Error"}, status = status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        person = list(persona.objects.filter(id=id).values())
        if len(person)>0:
            persona.objects.filter(id=id).delete()
            return Response({"mensaje" : "una persona se elimino"}, status = status.HTTP_204_NO_CONTENT)
        else:
            return Response({"mensaje" : "Error"}, status = status.HTTP_200_OK)
