from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from .models import *
import datetime

# Create your views here.
#class ShopUnitImportRequestView(generics.ListAPIView):
#    queryset = ShopUnitImportRequest.objects.all()
#    serializer_class = ShopUnitImportRequestSerializer

class import_view(APIView):
    def get(self, request):
        return Response({'test': 'get'})

    def post(self, request):
        for item in request.data['items']:
            try:
                shop_unit_import = ShopUnitImport.objects.create(
                        id=item['id'],
                        name=item['name'],
                        parentID=ShopUnit.objects.get(parentID=item['parentId']),
                        type=ShopUnitType[item['type']],
                        price=item['price'],
                      )
            except Exception as error:
                print(error)
                return Response({
                  'code': 400,
                  "message": "Невалидная схема документа или входные данные не верны."
                  })
        return Response({
                    'code': 200,
                    "message": "Вставка или обновление прошли успешно."
                    })
