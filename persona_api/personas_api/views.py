from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from personas_api.models import persona
from personas_api.serializer import persona_serializer

# Create your views here.

class persona_view(APIView):
    def post(self,request):
        serializer = persona_serializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje" : "persona se guardo"}, status = status.HTTP_201_CREATED)
        else:
            return Response({"mensaje" : "Error"}, status = status.HTTP_400_BAD_REQUEST)

    def get(self,request,id=None):
        if id:
            persona = persona.objects.get(id=id)
            serializer = persona_serializer(persona)
            return Response({"mensaje" : "persona econtrada", "persona" : serializer.data}, status = status.HTTP_200_OK)
        else:
            persona = persona.objects.all()
            serializer = persona_serializer(persona)
            return Response({"mensaje" : "persona econtrada", "persona" : serializer.data}, status = status.HTTP_200_OK)
