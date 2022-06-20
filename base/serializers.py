from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import Serializer
from .models import *


class UserSerializer(ModelSerializer):
    class Meta:
        
        model = User
        fields = ['name', 'email']


class CategorySerializer(ModelSerializer):
    class Meta:

        model = Category
        fields = '__all__'


class  SubCategorySerializer(ModelSerializer):
    class Meta:

        model = SubCategory
        fields = '__all__'


class TypeSerializer(ModelSerializer):
    class Meta:

        model = Type
        fields = '__all__'


class RegionSerializer(ModelSerializer):
    class Meta:

        model = Region
        fields = '__all__'


class SubRegionSerializer(ModelSerializer):
    class Meta:

        model = SubRegion
        fields = '__all__'


class VehicleSerializer(ModelSerializer):
    class Meta:

        model = Vehicle
        fields = '__all__'


class PropertySerializer(ModelSerializer):
    class Meta:

        model = Property
        fields = '__all__'


class ElectronicSerialaizer(ModelSerializer):
    class Meta:

        Model = Electronic
        fields = '__all__'


class ClothingAndBeautySerializer(ModelSerializer):
    class Meta:

        model = ClothingAndBeauty
        fields = '__all__'


class JobSerializer(ModelSerializer):
    class Meta:

        model = Job
        fields = '__all__'


class PetSerializer(ModelSerializer):
    class Meta:

        model = Pet
        fields = '__all__'