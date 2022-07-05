from app_image.models import ClothingAndBeautyImage, ElectronicImage, JobImage, PetImage, PropertyImage, VehicleImage
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import Serializer
from .models import *



class VehicleImageSerilaizer(ModelSerializer):
    class Meta:
        model = VehicleImage
        fields = '__all__'


class PropertyImageSerializer(ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = '__all__'


class ElectronicImageSerializer(ModelSerializer):
    class Meta:
        model = ElectronicImage
        fields = '__all__'


class ClothingAndBeautyImageSerializer(ModelSerializer):
    class Meta:

        model = ClothingAndBeautyImage
        fields = '__all__'


class JobImageSerializer(ModelSerializer):
    class Meta:

        model = JobImage
        fields = '__all__'


class PetImageSerializer(ModelSerializer):
    class Meta:

        model = PetImage
        fields = '__all__'
    




