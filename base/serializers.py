from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import Serializer
from .models import *
from app_image.serializers import *


class EagerLoadingMixin:
    @classmethod
    def setup_eager_loading(cls, queryset):
        """
        This function allow dynamic addition of the related objects to
        the provided query.
        @parameter param1: queryset
        """

        if hasattr(cls, "select_related_fields"):
            print(cls)
            queryset = queryset.select_related(*cls.select_related_fields)
        if hasattr(cls, "prefetch_related_fields"):
            queryset = queryset.prefetch_related(*cls.prefetch_related_fields)
        return queryset


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email']


class CategorySerializer(ModelSerializer):
    class Meta:

        model = Category
        # fields = '__all__'
        # exclude = ('slug', 'id')
        exclude = ('id', )
    
    @staticmethod
    def setup_eager_loading(queryset):
        print('dddd')
        queryset = queryset.defer('slug', 'id')
        return queryset

    # def save(self):
    #     print(self.context)
    #     x = self.context['request']
    #     print('************************')
    #     print(x)
        
    

class  SubCategorySerializer(ModelSerializer):
    category = CategorySerializer(many=False, read_only=True)

    class Meta:
        model = SubCategory
        fields = '__all__'
    
    # @staticmethod
    # def setup_eager_loading(queryset):
    #     queryset = queryset.select_related('category', )
    #     # queryset = queryset.select_related('subcategory')
    #     return queryset
    

class CategoryAndItsSubcategoriesSeriaizer(ModelSerializer):
    subcategory = SubCategorySerializer(many=True, read_only=False)

    class Meta:
        model = Category
        fields = '__all__'
    
    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.prefetch_related('subcategory')
        return queryset
    

class TypeSerializer(ModelSerializer):
    class Meta:

        model = Type
        fields = '__all__'
    
    # @staticmethod
    # def setup_eager_loading(queryset):
    #     queryset = queryset.select_related('sub_category__category')
    #     return queryset



class RegionSerializer(ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class SubRegionSerializer(ModelSerializer):
    region = RegionSerializer(many=False, read_only=True)

    class Meta:
        model = SubRegion
        fields = '__all__'
    
    # @staticmethod
    # def setup_eager_loading(queryset):
    #     queryset = queryset.select_related('region')
    #     return queryset

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
    category = SubCategorySerializer(many=False, read_only=True)

    class Meta:
        model = Vehicle
        fields = '__all__'


class PropertySerializer(ModelSerializer):
    property_image = PropertyImageSerializer(many=True, read_only=True)
    postered_by = UserSerializer(many=False, read_only=True)
    category = SubCategorySerializer(many=False, read_only=True)

    class Meta:
        model = Property
        fields = '__all__'


class ElectronicSerializer(ModelSerializer): #, EagerLoadingMixin):
    electronic_image = ElectronicImageSerializer(many=True, read_only=True)
    # postered_by = UserSerializer(many=False)
    # subcategory = SubCategorySerializer(many=False, read_only=True)

    # select_related_fields = ('postered_by', ) #('subcategory', 'type', 'subregion', 'postered_by')
    # prefetch_related_fields = ('electronic_image', )  # Only necessary if you have fields to prefetch

    class Meta:
        model = Electronic
        fields = '__all__'
        # exclude = ('subcategory', 'type')
        # fields = ['id', 'name', 'electronic_image']
    
    def to_representation(self, instance):
        self.fields['postered_by'] = UserSerializer()
        self.fields['subcategory'] = SubCategorySerializer()
        return super(ElectronicSerializer, self).to_representation(instance)
    
    # !ATTENTION: DO THIS FOR ALL ALL THE OTHER CATEGORIES
    @staticmethod
    def setup_eager_loading(queryset):
        # queryset = queryset.prefetch_related('electronic_image', )#, 'type', 'subregion',)
        # queryset = queryset.select_related('postered_by', )# 'subcategory')
        # queryset = queryset.select_related('subcategory__category', )
        queryset = queryset.select_related('subcategory__category', 'postered_by',)
        queryset = queryset.prefetch_related('electronic_image', )#, 'type', 'subregion',)
        
        # queryset = queryset.select_related('subcategory').select_related('subcategory')
        return queryset
    
    # Use this method to do other quesries
    @staticmethod
    def setup_eager_loading1(queryset):
        queryset = queryset.select_related('postered_by', 'subcategory__category')
        queryset = queryset.prefetch_related('electronic_image', )#, 'type', 'subregion',)
       
        # queryset = queryset.select_related('subcategory').select_related('subcategory')
        return queryset
    


class ClothingAndBeautySerializer(ModelSerializer):
    clothingandbeauty_image = ClothingAndBeautyImageSerializer(many=True, read_only=True)
    postered_by = UserSerializer(many=False, read_only=True)
    category = SubCategorySerializer(many=False, read_only=True)

    class Meta:
        model = ClothingAndBeauty
        fields = '__all__'


class JobSerializer(ModelSerializer):
    job_image = JobImageSerializer(many=True, read_only=True)
    postered_by = UserSerializer(many=False, read_only=True)
    category = SubCategorySerializer(many=False, read_only=True)

    class Meta:
        model = Job
        fields = '__all__'


class PetSerializer(ModelSerializer):
    pet_image = PetImageSerializer(many=True, read_only=True)
    postered_by = UserSerializer(many=False, read_only=True)
    category = SubCategorySerializer(many=False, read_only=True)

    class Meta:
        model = Pet
        fields = '__all__'


# class CategoryProductsAndSubcategorySerializer(Serializer):
#     # def __init__(self, ob, category_name):
#     def __init__(self, *args, **kwargs ):    
#         # super().__init__(ob)
#         super().__init__(*args, **kwargs)
#         # if category_name == 'Electronics':
#         if args[1] == 'Electronics':    
#             print('yess')
# #             category_product = ElectronicSerializer(many=True, read_only=True)
# #         # elif category_name == 'Vehicles':
# #         #     category_product = VehicleSerializer(many=True, read_only=True)
# #         # # Do it for the rest of the categories
# #             # subcategory = SubCategorySerializer(many=True, read_only=True)
# #         subcategory = SubCategorySerializer(many=True, read_only=True)

            
class ElectronicProductsAndSubcategorySerializer(Serializer):
    category_product = ElectronicSerializer(many=True, read_only=True)
    subcategory = SubCategorySerializer(many=True, read_only=True)
    type = TypeSerializer(many=True, read_only=True)


class VehicleProductsAndSubcategorySerializer(Serializer):
    category_product = VehicleSerializer(many=True, read_only=True)
    subcategory = SubCategorySerializer(many=True, read_only=True)
    type = TypeSerializer(many=True, read_only=True)


class PropertyProductsAndSubcategorySerializer(Serializer):
    category_product = PropertySerializer(many=True, read_only=True)
    subcategory = SubCategorySerializer(many=True, read_only=True)
    type = TypeSerializer(many=True, read_only=True)


class ClothingAndBeautyProductsAndSubcategorySerializer(Serializer):
    category_product = ClothingAndBeautySerializer(many=True, read_only=True)
    subcategory = SubCategorySerializer(many=True, read_only=True)
    type = TypeSerializer(many=True, read_only=True)


class JobProductsAndSubcategorySerializer(Serializer):
    category_product = JobSerializer(many=True, read_only=True)
    subcategory = SubCategorySerializer(many=True, read_only=True)
    type = TypeSerializer(many=True, read_only=True)


class PetProductsAndSubcategorySerializer(Serializer):
    category_product = PetSerializer(many=True, read_only=True)
    subcategory = SubCategorySerializer(many=True, read_only=True)
    type = TypeSerializer(many=True, read_only=True)


class ElectronicProductsAndItsRelatedProducts(Serializer):
    product = ElectronicSerializer(many=False, read_only=True)
    related_products = ElectronicSerializer(many=True, read_only=True)


class VehicleProductsAndItsRelatedProducts(Serializer):
    product  =VehicleSerializer(many=False, read_only=True)
    related_products = VehicleSerializer(many=True, read_only=True)


class PropertyProductsAndItsRelatedProducts(Serializer):
    product = PropertySerializer(many=False, read_only=True)
    related_products = PropertySerializer(many=True, read_only=True)


class ClothingAndBeautyProductsAndItsRelatedProducts(Serializer):
    product  =ClothingAndBeautySerializer(many=False, read_only=True)
    related_products = ClothingAndBeautySerializer(many=True, read_only=True)


class JobProductsAndItsRelatedProducts(Serializer):
    product = JobSerializer(many=False, read_only=True)
    related_products = JobSerializer(many=True, read_only=True)


class PetProductsAndItsRelatedProducts(Serializer):
    product = PetSerializer(many=False, read_only=True)
    related_products = PetSerializer(many=True, read_only=True)