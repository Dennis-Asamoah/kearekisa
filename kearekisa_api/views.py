from rest_framework.views import APIView
from rest_framework import status
from rest_framework import  generics
from rest_framework.response import Response
from base.models import * 
from base.serializers import *
from .utilities import *

class ListCategories(APIView):
    # queryset = Category.objects.all()
    # serializer_class = CategorySerializer
    categories = Category.objects.all()

    def get(self, request):
        serializer = CategorySerializer(self.categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RetrieveCategory(APIView):
    def get(self, request, slug):
        category = Category.objects.get(slug=slug)
        subcategories = category.subcategory_set.all()
        serializer = CategorySerializer(subcategories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RetrieveSubCategory(APIView):
    def get(self, request, slug):
        subcategory = SubCategory.objects.get(slug=slug)
        types = subcategory.type_set.all()
        serializer = TypeSerializer(types, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RetrieveType(APIView):
    mapper = {'Pet':PetSerializer, 'Electronics':ElectronicSerializer}

    def get(self, request, slug):
        # c_type = Type.objects.get(slug=slug)
        # mapper2= {'Pet':c_type.pet_set.all, 'Electronics':c_type.electronic_set.all}
        item = product_type(slug)  
        #  aa = c_type.pet_set.all()
        # x = c_type.sub_category.category.name
        #  products = c_type.pet_set.all()
        # products = mapper2[x]()
        products = item[0]()
        serializer = self.mapper[item[1]](products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ListRegions(APIView):
    def get(self, request):
        region = Region.objects.all()
        serializer = RegionSerializer(region, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RetrieveRegion(APIView):
    def get(self, request, slug):
        region = Region.objects.get(slug=slug)
        subregions = region.region.all()
        serializer = SubRegionSerializer(subregions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Test(APIView):
    def get(self, request, slug):
        region = Region.objects.get(slug=slug)
        #  x = region.region.all()
        serializer = RegionSerializer1(region, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
