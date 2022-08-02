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
        # bad code : cache.get() makes a network trip and it has unncessarily
        # been called twice which  means 2 round trips
        # YOU MUST CORRECT IT  
        # if cache.get('list_all_categories') is not None:
        #     print('yesss')
        #     serializer_data = cache.get('list_all_categories')
        #     return Response(serializer_data, status=status.HTTP_200_OK)
        
        cached_category_name = 'list_all_categories'
        product_json = cache.get(cached_category_name)
        if product_json:
            print(product_json)
            print(type(product_json))
            return Response(product_json, status=status.HTTP_200_OK)
        else:
            serializer = CategorySerializer(self.categories, many=True)
            cache.set('list_all_categories', serializer.data, None)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    # def post(self,request):
    #     zz = request.FILES.get('image')
    #     print(zz.name)
    #     print(zz.size/(1024))
    #     print(dir(zz))
    #     raise(10)
    #     s = CategorySerializer(data=request.data, context={'request': request})
    #     if s.is_valid():
    #         # s.save(slug = 'koonana')
    #         s.save() 
    #     return  Response(json.dumps('cool'))
        
        
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
        # category_object = category_products(slug)
        # category = category_object[0]()
        # # serializer = self.category_serializers[category_object[1]](category, many=True)
        # # print(serializer.data)
        # # return Response(serializer.data, status=status.HTTP_200_OK)
        
        # # optimized query with select_related and prefetch_related 
        # # Todo1: use model.objects.x  x=(defer,only) o optimize more
        # # Todo2: manipulate the slug to cache effectively all the 6 or more categoies 
        # category = self.category_serializers[category_object[1]].setup_eager_loading(category)
        # serializer = self.category_serializers[category_object[1]](category, many=True)
        # # print(serializer)
        # return Response(serializer.data, status=status.HTTP_200_OK)


        cached_category_name = 'list_of_'+slug+'_products'
        product_json = cache.get(cached_category_name)
        if product_json:
            print(product_json[0])
            return Response(product_json)
        else:
            category_object = category_products(slug)
            category = category_object[0]()
            category = self.category_serializers[category_object[1]].setup_eager_loading(category)
            serializer = self.category_serializers[category_object[1]](category, many=True)
            serializer_data = serializer.data
            cache.set(cached_category_name, serializer_data, None)
            return Response(serializer_data)
    
    
    # request.POST must contain category,subcategory,name
    def post(self, request, slug):
        # data = request.data
        # c =request.POST
        # print(c)
        # xx = request.FILES.getlist('sss')
        # print(xx)
        # print(data)
        # print(request.data.get('name'))
        post_product(request, slug)  # inserts request.POST(ie data) and request.FILES(ie files) into db. 
        return  Response('hi', status=status.HTTP_200_OK)
        # overwrite cache 


        # TODO invalidate cache item when post is added by both a user and an admin
        

class ListCategoriesAndItsSubcategories(APIView):
    """
      This endpoint lists all categories and the subcategories associated with them.
      eg Electronic Category contains TV and visuals, phones and tablets, etc 
      as subcategories. 
    """
    def get(self, request):
        # category = Category.objects.all()
        # # category = Category.objects.all().prefetch_related('subcategory')
        # queryset = CategoryAndItsSubcategoriesSeriaizer.setup_eager_loading(category)
        # # serializer = CategoryAndItsSubcategoriesSeriaizer(category, many=True)
        # serializer = CategoryAndItsSubcategoriesSeriaizer(queryset, many=True)
        # # serializer = CategoryAndItsSubcategoriesSeriaizer(category, many=True)
        # return  Response(serializer.data, status=status.HTTP_200_OK)
        
        name = 'categories_and_its_subcategories_data'
        cached_category_data = cache.get(name)
        if cached_category_data:
            return Response(cached_category_data)
        else:
            category = Category.objects.all()
            queryset = CategoryAndItsSubcategoriesSeriaizer.setup_eager_loading(category)
            serializer = CategoryAndItsSubcategoriesSeriaizer(queryset, many=True)
            serializer_data = serializer.data
            cache.set(name, serializer_data, None)
            return  Response(serializer_data, status=status.HTTP_200_OK)
        
        # IF ITEMS ARE CHANGED (CATEGORIES AND ITS SUNBATEGORIES) ARE MODIFIED BY THE ADMIN,
        # IT WON'T REFLECT ON THE CACHE. UNLESS YOU WARM THE CACHE DB with a
        # THE MODIFIES. 



        
class RetrieveSubcategoriesOfCategory(APIView):
    """
      This endpoint lists all subcategories associated with a particular 
      category. Eg when slug=electronics,  all subcategories 
      associated with electronics will be listed.
      eg Electronics will list TV and visuals,etc as ucategories. 
    """
    def get(self, request, slug):
        # category = Category.objects.get(slug=slug)
        # # category = Category.objects.get(slug=slug)
        # subcategories = category.subcategory.all()
        # # queryset = SubCategorySerializer.setup_eager_loading(subcategories)
        # serializer = SubCategorySerializer(subcategories, many=True)
        # return Response(serializer.data, status=status.HTTP_200_OK)
        
        cache_name = 'retrieve_subcategory_of_'+slug 
        cached_data = cache.get(cache_name)
        if cached_data:
            return Response(cached_data, status=status.HTTP_200_OK)
        else:
            category = Category.objects.get(slug=slug)
            subcategories = category.subcategory.all()
            serializer = SubCategorySerializer(subcategories, many=True)
            serializer_data = serializer.data
            cache.set(cache_name, serializer_data, None)
            return Response(serializer_data, status=status.HTTP_200_OK)

            # TODO : DO NOT FORGET TO UPDATE THE CACHE WHEN SUBCATEGORY IS A DDED TP A CATEGORY


class RetrieveTypesOfSubCategory(APIView):
    """
      This endpoint lists all the types associated with a  partticular
      subcategory. eg the subcategory 'phones and tablets' will list 
      'Apple','samsung phone and tablets'. Like wise 'Tv and visuals'
      wil list 'samsung flatscreen tv'
    """
    def get(self, request, slug):
        # subcategory = SubCategory.objects.get(slug=slug)
        # # subcategory = SubCategory.objects.select_related('category').get(slug=slug)
        # types = subcategory.type_set.all()
        # # types = TypeSerializer.setup_eager_loading(types)
        # serializer = TypeSerializer(types, many=True)
        # return Response(serializer.data, status=status.HTTP_200_OK)

        cache_name = 'retrieve_types_of_'+slug
        cached_data = cache.get(cache_name)
        if cached_data:
            return Response(cached_data, status=status.HTTP_200_OK)
        else:
            subcategory = SubCategory.objects.get(slug=slug)   
            types = subcategory.type_set.all()  
            serializer = TypeSerializer(types, many=True)
            serializer_data = serializer.data
            cache.set(cache_name, serializer_data, None) #  None makes sure data persists.
            return Response(serializer_data, status=status.HTTP_200_OK)
        
        # TODO: DO NOT FORGET TO UPDATE THE CACHE IF A TYPE IS ADDED TO A SUBCATEGORY

        
# lists all the products of a subcategory without filtering
class ListSubCategoryProducts(APIView):
    """ 
    This endpoint is used to list all  the products under a subcategory.
    eg if a subcategory  is  'cell-phones-and-tablets', then all products under
    this subcategory will be listed . In this case all samsung, iphones, oppo and 
    other phone brands will all be listed without any filtering whatsoever

    """
    category = {'Electronics': ElectronicSerializer, 'Pet': PetSerializer}

    def get(self, request, slug):
        # print(request.GET)
        # print(request.data)
        # print(request.body)
        # # subcategory = SubCategory.objects.get(slug=slug)
        # # category_name = subcategory.category.name
        # item = subcategory_product(slug)
        # products = item[0]() #  .filter(electronic_model="S6")
        # # x = exec("electronic_model='S6'")
        # # print (x)
        # #  products = item[0]().filter(**request.data)
        
        # serializer = self.category[item[1]].setup_eager_loading(products)#, many=True)
        # serializer = self.category[item[1]](serializer, many=True)
        # return Response(serializer.data, status=status.HTTP_200_OK)

        cache_name = 'list_'+slug+'_products'
        cached_data = cache.get(cache_name)
        if cached_data:
            return Response(cached_data, status=status.HTTP_200_OK)
        else:
            item = subcategory_product(slug)
            products = item[0]() #  .filter(electronic_model="S6")
            serializer = self.category[item[1]].setup_eager_loading(products)#, many=True)
            serializer = self.category[item[1]](serializer, many=True)
            serializer_data = serializer.data
            cache.set(cache_name, serializer_data, None)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        # TODO: Must update cache when item is added. You may check product_category, product_subcategory
        # and product_type to update the cache or you may end up with stale data. You can also delte 
        # a key accordingly , but this can cause a cache stampede if a lot of requests appear at the same time. 


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
        # data_for_filtering = request.data
        # item = subcategory_product(slug)
        # products = item[0]().filter(**{"name": "Samsung galaxy S6"})
        # # optimizes the query. Reduces number of ntework trips from or sql queries 
        # # frim 23 to only 4.
        # products =  self.category[item[1]].setup_eager_loading(products)
        # serializer = self.category[item[1]](products, many=True)
        # return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, slug):
        data_for_filtering = request.data
        item = subcategory_product(slug)
        products = item[0]().filter(**data_for_filtering)
        # optimizes the query. Reduces number of ntework trips from or sql queries 
        # frim 23 to only 4.
        products =  self.category[item[1]].setup_eager_loading(products)
        serializer = self.category[item[1]](products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
        # No need to cache the filtering as there are way too many ways to filter 
        # products

class ListType(APIView):
    """
       This endpoint lists all products asscociated with a type.
       eg a type 'apple' will list all apple products which includes the
       samsung phones etc
    """
    category_serializers = {'Pet': PetSerializer, 'Electronics': ElectronicSerializer}

    def get(self, request, slug):
        # # c_type = Type.objects.get(slug=slug)
        # # mapper2= {'Pet':c_type.pet_set.all, 'Electronics':c_type.electronic_set.all}
        # item = product_type(slug)  
        # #  aa = c_type.pet_set.all()
        # # x = c_type.sub_category.category.name
        # #  products = c_type.pet_set.all()
        # # products = mapper2[x]()
        # products = item[0]()
        # products = self.category_serializers[item[1]].setup_eager_loading(products)
        # serializer = self.category_serializers[item[1]](products, many=True)
        # return Response(serializer.data, status=status.HTTP_200_OK)

        cache_name = 'retrieve_'+'type_'+slug
        cached_data = cache.get(cache_name)
        if cached_data:
            return Response(cached_data, status=status.HTTP_200_OK)
        else:        
            item = product_type(slug)  
            products = item[0]()
            products = self.category_serializers[item[1]].setup_eager_loading(products)
            serializer = self.category_serializers[item[1]](products, many=True)
            serializer_data = serializer.data
            cache.set(cache_name, serializer_data, None)
            return Response(serializer_data, status=status.HTTP_200_OK)
        
        # TODO: find a way to update this cache when a product under this type is updated. ir
        # products with a artcular type is update


class ListRegions(APIView):
    def get(self, request):
        # region = Region.objects.all()
        # serializer = RegionSerializer(region, many=True)
        # return Response(serializer.data, status=status.HTTP_200_OK)

        cache_name = 'list_regions'
        cached_data = cache.get(cache_name)
        if cached_data:
            return Response(cached_data, status=status.HTTP_200_OK)
        else:
            region = Region.objects.all()
            serializer = RegionSerializer(region, many=True)
            serializer_data = serializer.data
            cache.set(cache_name, serializer_data, None)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        # DO NOT FORGET TO UPDATE CACHE IF A REGION IS ADDED

    
    # delete later. It was just for testing 
    def post(self, request):
        data = request.data
        serializer = RegionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response('correct',)
        else:
            return Response('not correct')


class ListSubregions(APIView):
    def get(self, request, slug):
        # region = Region.objects.get(slug=slug)
        # # region = Region.objects.prefetch_related('region__region').get(slug=slug)
        # subregions = region.region.all()
        # # subregions = SubRegionSerializer.setup_eager_loading(subregions)
        # serializer = SubRegionSerializer(subregions, many=True)
        # return Response(serializer.data, status=status.HTTP_200_OK)

        cache_name = 'list_'+slug+'_subregions'
        cached_data = cache.get(cache_name)
        if cached_data:
            return Response(cached_data, status=status.HTTP_200_OK)
        else:
            region = Region.objects.get(slug=slug)
            subregions = region.region.all()
            serializer = SubRegionSerializer(subregions, many=True)
            serializer_data = serializer.data
            cache.set(cache_name, serializer_data, None)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        # DO NOT FORGET TO UPDATE CACHE IF A SUBREGION IS ADDED


class Test(APIView):
    def get(self, request, slug):
        region = Region.objects.get(slug=slug)
        #  x = region.region.all()
        serializer = RegionSerializer1(region, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ListCategoryProductsAndSubcategory(APIView):
    """ 
        This endpoints lists all the products in a  category irrespective of their  subcategories
        or type. It the lists their subcategories belonging this category:
        The json file will look like
        {
             products: [
                {},
                {}
             ],
             subcategories: [
                {},
                {}
             ]
        }
        This as a reulst of combined serializers using namedtuple.
     """
    categories = {
        'Electronics': ElectronicProductsAndSubcategorySerializer,
        'Pet': PetProductsAndSubcategorySerializer,
        # DO NOT FORGET TO PUT THE REST (IE hechicles,propers,clothing and job)
    }

    def get(self, request, slug):
        # category_products, subcategory, category_name = category_product_and_sub(slug)
        # # category_products, subcategory =  category_products(), subcategory()
        # # print(category_products)
        # # print(subcategory)
        # data = CategoryProductsAndSub(category_product=category_products, subcategory=subcategory, type=None)
        # # print(data)
        # # serializer = CategoryProductsAndSubcategorySerializer(data) #, category_name)
        # serializer = self.categories[category_name](data)  # , category_name)
        # print(serializer)
        # # print(serializer.data)
        # return Response(serializer.data, status=status.HTTP_200_OK)

        cache_name = 'list_'+slug+'_products_and_its_subcategories'
        cached_data = cache.get(cache_name)
        if cached_data:
            return Response(cached_data, status=status.HTTP_200_OK)
        else:
            category_products, subcategory, category_name = category_product_and_sub(slug)
            data = CategoryProductsAndSub(category_product=category_products, subcategory=subcategory, type=None)
            serializer = self.categories[category_name](data) 
            serializer_data = serializer.data
            cache.set(cache_name, serializer_data, None)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        # NB: DO NOT FORGET TO UPDATE CACHE IF A PRODUCT IS ADDED TO THE CATEGORY 


class ListSubCategoryProductsAndTypes(APIView):
    """
        This endpoints lists all the products in a  particular subcategory  together with
        the types associated with this subcategory:
        The json file will look like
        {
             products: [
                {},
                {}
             ],
             types: [
                {},
                {}
             ]
        }
        This as a reulst of combined serializers using namedtu[ple.
        
    """
    categories = {
        'Electronics': ElectronicProductsAndSubcategorySerializer,
        'Pet': PetProductsAndSubcategorySerializer,
        # DO NOT FORGET TO PUT THE REST (IE hechicles,propers,clothing and job)
    }

    def get(self, request, slug):
        # subcategory_product, product_type, category_name = subcategory_product_and_types(slug)
        # data = CategoryProductsAndSub(category_product=subcategory_product, subcategory=None, type=product_type)
        # serializer = self.categories[category_name](data)
        # return  Response(serializer.data, status=status.HTTP_200_OK)

        cache_name = 'list_'+slug+'_products_and_types'
        cached_data = cache.get(cache_name)
        if cached_data:
            return Response(cached_data, status=status.HTTP_200_OK)
        else:
            subcategory_product, product_type, category_name = subcategory_product_and_types(slug)
            data = CategoryProductsAndSub(category_product=subcategory_product, subcategory=None, type=product_type)
            serializer = self.categories[category_name](data)
            serializer_data = serializer.data
            cache.set(cache_name, serializer_data, None)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        # # NB: DO NOT FORGET TO UPDATE CACHE IF A PRODUCT  OR TYPE IS UNDER THIS SUBCATEGORY IS ADDED
        # # IE UPDATE CACHE ID TYPE OR PRODUCT IS CHANGED 


class RetrieveProduct(APIView):
    """
        This endpoint list the details of a particular product together with similar products 
        associated with this particular product. 
    """
    serializers = {
        'Electronics': ElectronicProductsAndItsRelatedProducts,
        'Pet': PetProductsAndItsRelatedProducts,
         # Do not forget to do it for the rest of the categories
    }

    # def get(self, request, category_slug, subcategory_slug, product_slug):
    def get(self, request, category_slug, subcategory_slug, product_slug):
        # product, related_products, product_name = product_and_related_prouducts(category_slug, product_slug)
        # combined_data = ProductAndItsRelatedProducts(product=product, related_products=related_products)
        # serializer = self.serializers[product_name](combined_data)
        # return Response(serializer.data, status=status.HTTP_200_OK)

        cache_name = category_slug  + '_' + subcategory_slug + '_' + product_slug
        cached_data = cache.get(cache_name)
        if cached_data:
            print(1234)
            return Response(cached_data, status=status.HTTP_200_OK)
        else:
            print(123456)
            product, related_products, product_name = product_and_related_prouducts(category_slug, product_slug)
            combined_data = ProductAndItsRelatedProducts(product=product, related_products=related_products)
            serializer = self.serializers[product_name](combined_data)
            serializer_data = serializer.data
            cache.set(cache_name, serializer.data, 300) # 60*5=300 TTL
            return Response(serializer_data, status=status.HTTP_200_OK)


