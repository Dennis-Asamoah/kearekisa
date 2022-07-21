import json
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import  generics
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.pagination import PageNumberPagination
from django.core.cache import cache 
from base.models import * 
from base.serializers import *
from .utilities import *

# Serializer Pagina 
class koo(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    # max_page_size = 50
    # page_query_param = 'p'

    # def get_paginated_response(self, data):
    #     response = Response(data)
    #     response['count'] = self.page.paginator.count
    #     response['next'] = self.get_next_link()
    #     response['previous'] = self.get_previous_link()
    #     return response



class ListCategories(APIView):
    """
       This endpoint lists all the different categories.The categories are 
       **Electronics
       **Vehicles
       **ClothingAndBeautys
       **Pets
       **Jobs
       **Properties
    """
    # queryset = Category.objects.all()
    # serializer_class = CategorySerializer
    categories = Category.objects.all()#('slug') #
    # pagination_class = PageNumberPagination

    def get(self, request, format=None):
        # paginator = koo()
        # categories = paginator.paginate_queryset(self.categories, request)
        # serializer = CategorySerializer(categories, many=True, context={'request': 12})
        # return paginator.get_paginated_response(serializer.data)
        ## serializer = CategorySerializer(self.categories, many=True)
        # -- editing response headers
        # response = Response(serializer.data, status=status.HTTP_200_OK)
        # response['nanme'] = 'Dennis'
        # return response
        ## return Response(serializer.data, status=status.HTTP_200_OK)


        # serializer = CategorySerializer.setup_eager_loading(Category.objects)
        # serializer = CategorySerializer(serializer, many=True)
        # return Response(serializer.data, status=status.HTTP_200_OK)

        # cache results 
        if cache.get('list_all_categories') is not None:
            print('yesss')
            serializer_data = cache.get('list_all_categories')
            return Response(serializer_data, status=status.HTTP_200_OK)
            
        else:
            serializer = CategorySerializer(self.categories, many=True)
            cache.set('list_all_categories', serializer.data, None)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        
class ListCategoryProducts(APIView):
    """
       This endpoint lists all the products under a category irrespective of its subcategory of type.
       In order words 'We fetch all products that is found in  a particular category'.

       eg samsung phone, iphone and samsung flatscreen are all under the electronics category
       even though they are under different subcategories. ie samsung phone and iphone are under 
       subcategory 'phone and tablet' and samsung flatcreen ty is under 'TV and visuals' .
    """
    # parser_classes = [MultiPartParser, FormParser]

    category_serializers = {
        'Electronics': ElectronicSerializer, 
        'Vehicles': VehicleSerializer
        }
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request, slug):
        category_object = category_products(slug)
        category = category_object[0]()
        # serializer = self.category_serializers[category_object[1]](category, many=True)
        # print(serializer.data)
        # return Response(serializer.data, status=status.HTTP_200_OK)
        
        # optimized query with select_related and prefetch_related 
        # Todo1: use model.objects.x  x=(defer,only) o optimize more
        # Todo2: manipulate the slug to cache effectively all the 6 or more categoies 
        category = self.category_serializers[category_object[1]].setup_eager_loading(category)
        serializer = self.category_serializers[category_object[1]](category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



        # if cache.get('list_category_products') is not None:
        #     pass  
 
    # request.POST must contain category,subcategory,name
    def post(self, request, slug):
        # data = request.data
        # c =request.POST
        # print(c)
        # xx = request.FILES.getlist('sss')
        # print(xx)
        # print(data)
        # print(request.data.get('name'))
        post_product(request, slug)
        return  Response('hi', status=status.HTTP_200_OK)
        

class ListCategoriesAndItsSubcategories(APIView):
    """
      This endpoint lists all categories and the subcategories associated with them.
      eg Electronic Category contains TV and visuals, phones and tablets, etc 
      as subcategories. 
    """
    def get(self, request):
        category = Category.objects.all()
        queryset = CategoryAndItsSubcategoriesSeriaizer.setup_eager_loading(category)
        serializer = CategoryAndItsSubcategoriesSeriaizer(queryset, many=True)
        # serializer = CategoryAndItsSubcategoriesSeriaizer(category, many=True)
        return  Response(serializer.data, status=status.HTTP_200_OK)

        
class RetrieveSubcategoriesOfCategory(APIView):
    """
      This endpoint lists all subcategories associated with a particular 
      category. Eg when slug=electronics,  all subcategories 
      associated with electronics will be listed.
      eg Electronics will list TV and visuals,etc as ucategories. 
    """
    def get(self, request, slug):
        category = Category.objects.get(slug=slug)
        subcategories = category.subcategory.all()
        # queryset = SubCategorySerializer.setup_eager_loading(subcategories)
        serializer = SubCategorySerializer(subcategories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RetrieveTypesOfSubCategory(APIView):
    """
      This endpoint lists all the types associated with a  partticular
      subcategory. eg the subcategory 'phones and tablets' will list 
      'Apple','samsung phone and tablets'. Like wise 'Tv and visuals'
      wil list 'samsung flatscreen tv'
    """
    def get(self, request, slug):
        subcategory = SubCategory.objects.get(slug=slug)
        # subcategory = SubCategory.objects.select_related('category').get(slug=slug)
        types = subcategory.type_set.all()
        # types = TypeSerializer.setup_eager_loading(types)
        serializer = TypeSerializer(types, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# lists all the products of a subcategory without filtering
class RetrieveSubCategoryProducts(APIView):
    """ 
    This endpoint is used to list all  the products under a subcategory.
    eg if a subcategory  is  'cell-phones-and-tablets', then all products under
    this subcategory will be listed . In this case all samsung, iphones, oppo and 
    other phone brands will all be listed without any filtering whatsoever

    """
    category = {'Electronics': ElectronicSerializer, 'Pet': PetSerializer}

    def get(self, request, slug):
        print(request.GET)
        print(request.data)
        print(request.body)
        # subcategory = SubCategory.objects.get(slug=slug)
        # category_name = subcategory.category.name
        item = subcategory_product(slug)
        products = item[0]() #  .filter(electronic_model="S6")
        # x = exec("electronic_model='S6'")
        # print (x)
        #  products = item[0]().filter(**request.data)
       
        serializer = self.category[item[1]].setup_eager_loading(products)#, many=True)
        serializer = self.category[item[1]](serializer, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FilterProducts(APIView):
    """
        This class is the  similar to  the RetreiveSubcategoryProducts class
        with the exception that using the post method , we get the attributes  which
        will be used to filter products in a subcategory.  
        eg 
        data_to_be_used_for_filtering = request.data  # In a POST method
        subcategory = Subcategory.objects.get(slug=slug)
        # Since we will have a dictionary of keys-word arguments we use
        # ** wildcat for uppacking  eg x = {'arg1': 'value1', 'arg22': 'value2'} 
        # .filter(**x) == .filter(arg1=value1, arg2='value2')
        subcategory.electronics_set_all().filter(**data)

    """
    category = {'Electronics': ElectronicSerializer, 'Pet': PetSerializer}
    # the get method is used for manual testing purposes
    def get(self, request, slug):
        x = request.GET
        print(x)
        return Response(json.dumps('kio'), status=status.HTTP_200_OK)

    def post(self, request, slug):
        data_for_filtering = request.data
        item = subcategory_product(slug)
        products = item[0]().filter(**data_for_filtering)
        # optimizes the query. Reduces number of ntework trips from or sql queries 
        # frim 23 to only 4.
        products =  self.category[item[1]].setup_eager_loading(products)
        serializer = self.category[item[1]](products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
            

class RetrieveType(APIView):
    """
       This endpoint lists all products asscociated with a type.
       eg a type 'apple' will list all apple products which includes the
       samsung phones etc
    """
    category_serializers = {'Pet': PetSerializer, 'Electronics': ElectronicSerializer}

    def get(self, request, slug):
        # c_type = Type.objects.get(slug=slug)
        # mapper2= {'Pet':c_type.pet_set.all, 'Electronics':c_type.electronic_set.all}
        item = product_type(slug)  
        #  aa = c_type.pet_set.all()
        # x = c_type.sub_category.category.name
        #  products = c_type.pet_set.all()
        # products = mapper2[x]()
        products = item[0]()
        products = self.category_serializers[item[1]].setup_eager_loading(products)
        serializer = self.category_serializers[item[1]](products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ListRegions(APIView):
    def get(self, request):
        region = Region.objects.all()
        serializer = RegionSerializer(region, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # delete later. It was just for testing 
    def post(self, request):
        data = request.data
        serializer = RegionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response('correct',)
        else:
            return Response('not correct')


class RetrieveRegion(APIView):
    def get(self, request, slug):
        region = Region.objects.get(slug=slug)
        # region = Region.objects.prefetch_related('region__region').get(slug=slug)
        subregions = region.region.all()
        # subregions = SubRegionSerializer.setup_eager_loading(subregions)
        serializer = SubRegionSerializer(subregions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Test(APIView):
    def get(self, request, slug):
        region = Region.objects.get(slug=slug)
        #  x = region.region.all()
        serializer = RegionSerializer1(region, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ListCategoryProductsAndSubcategory(APIView):
    categories = {
        'Electronics': ElectronicProductsAndSubcategorySerializer,
        'Pet': PetProductsAndSubcategorySerializer,
        # DO NOT FORGET TO PUT THE REST (IE hechicles,propers,clothing and job)
    }

    def get(self, request, slug):
        category_products, subcategory, category_name = category_product_and_sub(slug)
        # category_products, subcategory =  category_products(), subcategory()
        # print(category_products)
        # print(subcategory)
        data = CategoryProductsAndSub(category_product=category_products, subcategory=subcategory, type=None)
        # print(data)
        # serializer = CategoryProductsAndSubcategorySerializer(data) #, category_name)
        serializer = self.categories[category_name](data)  # , category_name)
        print(serializer)
        # print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ListSubCategoryProductsAndTypes(APIView):
    categories = {
        'Electronics': ElectronicProductsAndSubcategorySerializer,
        'Pet': PetProductsAndSubcategorySerializer,
        # DO NOT FORGET TO PUT THE REST (IE hechicles,propers,clothing and job)
    }

    def get(self, request, slug):
        subcategory_product, product_type, category_name = subcategory_product_and_types(slug)
        data = CategoryProductsAndSub(category_product=subcategory_product, subcategory=None, type=product_type)
        serializer = self.categories[category_name](data)
        return  Response(serializer.data, status=status.HTTP_200_OK)


class RetrieveProduct(APIView):
    serializers = {
        'Electronics': ElectronicProductsAndItsRelatedProducts,
        'Pet': PetProductsAndItsRelatedProducts,
         # Do not forget to do it for the rest of the categories
    }

    # def get(self, request, category_slug, subcategory_slug, product_slug):
    def get(self, request, category_slug, subcategory_slug, product_slug):
        product, related_products, product_name = product_and_related_prouducts(category_slug, product_slug)
        combined_data = ProductAndItsRelatedProducts(product=product, related_products=related_products)
        serializer = self.serializers[product_name](combined_data)
        return Response(serializer.data, status=status.HTTP_200_OK)


