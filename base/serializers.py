from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import Serializer
from .models import *
from app_image.serializers import *

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
    region = RegionSerializer(many=False, read_only=True)

    class Meta:
        model = SubRegion
        fields = '__all__'


class RegionSerializer1(ModelSerializer):
    region = SubRegionSerializer(many=True, read_only=True)
    class Meta:
        model = Region
        fields = ['name', 'slug', 'region']


class ProductSerializer(ModelSerializer):
    class Meta:
        model  = Product
        fields = '__all__'


class VehicleSerializer(ModelSerializer):
    vehicle_image = VehicleImageSerilaizer(many=True, read_only=True)
    postered_by = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Vehicle
        fields = '__all__'


class PropertySerializer(ModelSerializer):
    property_image = PropertyImageSerializer(many=True, read_only=True)
    postered_by = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Property
        fields = '__all__'


class ElectronicSerializer(ModelSerializer):
    electronic_image = ElectronicImageSerializer(many=True, read_only=True)
    postered_by = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Electronic
        fields = '__all__'
        #  fields = ['id', 'name', 'electronic_image']


class ClothingAndBeautySerializer(ModelSerializer):
    clothingandbeauty_image = ClothingAndBeautyImageSerializer(many=True, read_only=True)
    postered_by = UserSerializer(many=False, read_only=True)

    class Meta:
        model = ClothingAndBeauty
        fields = '__all__'


class JobSerializer(ModelSerializer):
    job_image = JobImageSerializer(many=True, read_only=True)
    postered_by = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Job
        fields = '__all__'


class PetSerializer(ModelSerializer):
    pet_image = PetImageSerializer(many=True, read_only=True)
    postered_by = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Pet
        fields = '__all__'
