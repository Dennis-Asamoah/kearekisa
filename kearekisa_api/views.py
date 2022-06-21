from rest_framework.views import APIView
from rest_framework import status
from rest_framework import  generics
from rest_framework.response import Response
from base.models import * 
from base.serializers import *


class ListCategories(APIView):
    # queryset = Category.objects.all()
    # serializer_class = CategorySerializer
    categories = Category.objects.all()

    def get(self, request):
        serializer = CategorySerializer(self.categories, many=True)
        return Response(serializer.data)