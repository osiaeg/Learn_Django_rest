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
        if serializer.is_valid():
            serializer.save()
            return Response()
        else:
            return Response({
                "code": 400,
                "message": "Validation Failed"
                }, status=400)
