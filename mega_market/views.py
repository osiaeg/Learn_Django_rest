from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from .models import *
from .serializers import ShopUnitImportRequestSerializer
import datetime

# Create your views here.
#class ShopUnitImportRequestView(generics.ListAPIView):
#    queryset = ShopUnitImportRequest.objects.all()
#    serializer_class = ShopUnitImportRequestSerializer

class import_view(APIView):
    def post(self, request):
        serializer = ShopUnitImportRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Нужно дописать создание записи в базе данных

        return Response({'request': serializer.data})
