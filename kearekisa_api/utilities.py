# from base.models import Category, Electronic, Type
# from base.models import SubCategory
from collections import namedtuple
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.core.cache import cache
from base.models import *
from base.serializers import *
from app_image.models import *


electronic_subcategories = [
    'cell-phones-and-tablets',
    'tv-and-visuals',
]

property_subcategories = [

]

vehicle_subcategories = [

]

clothingandbeauty_subcategories = [

]

job_subcategories = [

]

pet_subcategories =[
    'catdog',

]


CategoryProductsAndSub = namedtuple('product_and_sub', ['category_product', 'subcategory', 'type'] )

ProductAndItsRelatedProducts = namedtuple('products_and_related_products', ['product', 'related_products'])


def product_type(slug):
    """
    """
    # item_type = Type.objects.get(slug=slug)
    item_type = Type.objects.select_related('sub_category__category').get(slug=slug)
    type_name = item_type.sub_category.category.name
    print(type_name)
    if type_name == 'Pet':
        return item_type.pet_set.all,type_name
        # return item_type.pet_set.select_related('subcategory__category').all, type_name
    elif type_name == 'Electronics':
        return item_type.electronic_set.all,type_name
        # return item_type.electronic_set.select_related('subcategory__category').all, type_name

def  subcategory_product(slug):
    subcategory = SubCategory.objects.select_related('category').get(slug=slug)
    # subcategory = SubCategory.objects.prefetch_related('electronic_set').get(slug=slug)
    category_name = subcategory.category.name
    if slug in electronic_subcategories:
        # print(subcategory.name)
        # print(456666666666666666666)
        # print(subcategory.type_set.all())
        return subcategory.electronic_set.all, category_name
    elif slug in property_subcategories:
        return subcategory.property_set.all, category_name
    elif slug in vehicle_subcategories:
        return subcategory.vehicle_set.all, category_name
    elif slug in clothingandbeauty_subcategories:
        return subcategory.property_set.all, category_name
    elif slug in job_subcategories:
        return subcategory.job_set.all, category_name
    else:
        return subcategory.pet_set.all, category_name

def category_products(slug):
    category = Category.objects.get(slug=slug)
    category_name = category.name
    if category_name == 'Electronics':
        return Electronic.objects.all, category_name
    elif category_name == 'Vehicles':
        return Vehicle.objects.all, category_name
    # do not forget to do it for the rest of the categories 

def category_product_and_sub(slug):
    category = Category.objects.prefetch_related('subcategory').get(slug=slug)
    category_name = category.name
    if category_name == 'Electronics':
        # return Electronic.objects.all(), category.subcategory.all(), category_name
        return Electronic.objects.select_related('subcategory__category', 'postered_by')\
            .prefetch_related('electronic_image'),\
               category.subcategory.all(), category_name
    elif category_name == 'Pet':
        return Pet.objects.all(), category.subcategory.all(), category_name
    # do not forget to do it for the rest of the categories

def subcategory_product_and_types(slug):
    # subcategory = SubCategory.objects.get(slug=slug)
    subcategory = SubCategory.objects.select_related('category').get(slug=slug)
    if slug in electronic_subcategories:
        # TODO: Repeat for the rest of the other categories or subcategories
        return subcategory.electronic_set.all().select_related('postered_by').prefetch_related('electronic_image'),\
             subcategory.type_set.all(), subcategory.category.name
    elif slug in pet_subcategories:
        return subcategory.pet_set.all(), subcategory.type_set.all(), subcategory.category.name

    # do not forget to do it for the rest of the categories

def product_and_related_prouducts(category_slug, product_slug):
    # category = Category.objects.get(slug=category_slug)
    category = Category.objects.get(slug=category_slug)
    category_name = category.name
    if category.name == 'Electronics':
        product = Electronic.objects.select_related('postered_by', 'subcategory__category')\
            .prefetch_related('electronic_image').get(slug=product_slug)
        related_products = Electronic.objects.select_related('postered_by', 'subcategory__category')\
            .prefetch_related('electronic_image').exclude(slug=product_slug)
        return product, related_products, category_name 
    elif category.name == 'Pets':
        product = Pet.objects.get(slug=product_slug)
        related_products  =Pet.objects.get(slug=product_slug)
        return product, related_products, category_name 
    # DO it for the rest  of the categories 

# This function is responsible for publishin new items.
def post_product(request, slug):
    data = request.POST
    print(data)
    images = request.FILES.getlist('image')
    combined_image_names = '-'.join([i.name for i in images ])
    # print(combined_image_names)
    # print(images)
    category = Category.objects.get(slug=slug)
    category_name = category.name
    if category.name == 'Electronics':
        # let save the data in the serialiser
        serializer = ElectronicSerializer(data=data)
        if serializer.is_valid():
            # serializer.save(image_urls=combined_image_names)
            serializer.save()
            # get obect with name,description and price
            # replace with uuid which is more secure 
            # you can put in try and except block but  will slow down programe alittle bit
            # THIS PIECE OF CODE IS VERY ERROR PRONE AND MUST BE RESOLVED
            print('5555555555555')
            product_object = Electronic.objects.get(name=request.POST.get('name'), 
            description=request.POST.get('description'),
            price=request.POST.get('price')
            )
            print(product_object)
            create_electronic_images = [
            ElectronicImage.objects.create(electronic=product_object,image=image) for image in images
            ]
        else:
            # Do something here 
            print(serializer.errors)



# def product_and_related_prouducts_refactored(category_slug, product_slug):
#     category = Category.objects.get(slug=category_slug)
#     category_name = category.name
#     product = category.
class PaginateProducts(PageNumberPagination):
    page_size = 2

    # def get_paginated_response(self, data):
    #     response = Response(data)
    #     response['count'] = self.page.paginator.count
    #     response['next'] = self.get_next_link()
    #     response['previous'] = self.get_previous_link()
    #     return response

def process_cache(request, cached_data, num, count):
    # page_num = '' if not get_page_num or get_page_num=='1' else get_page_num
    # if not page_num:
    #     cache_category_name = cache_name  # 'list_all_categories'
    #     num = 1
    # else:    
    #     num =  int(page_num)
    #     cache_category_name = 'list_all_categories' + page_num  # 'list_all_categories_page' + page_num 
    # print(cache_category_name)
    # cached_data = cache.get(cache_category_name)
    # if cached_data:
    #     print('here')
    #     print(cached_data)
    res = Response(cached_data)
    count1 = count if count%2==0 else count+1  # when product list are odd in size add 1 to it so that 
    # get last product . 

    if num>1 and num<=(count1//2):  # 2 only represents no of products shown on each paginated page.       
        next = num + 1
        if next > (count1//2):
            res['next'] = None
        else:
            res['next'] = request.build_absolute_uri('?page={}'.format(next))

        prev =  num - 1  
        request.build_absolute_uri('?page={}'.format(str(num)))
        res['count'] = count
        
        res['previous'] = request.build_absolute_uri('?page={}'.format(prev))
        # else:
        return res
    else:
        res['count'] = count
        next = num + 1
        res['next'] = request.build_absolute_uri('?page={}'.format(next))
        res['previous'] = None
        return res

def process_cache1(request, cached_data, num, count):
    # page_num = '' if not get_page_num or get_page_num=='1' else get_page_num
    # if not page_num:
    #     cache_category_name = cache_name  # 'list_all_categories'
    #     num = 1
    # else:    
    #     num =  int(page_num)
    #     cache_category_name = 'list_all_categories' + page_num  # 'list_all_categories_page' + page_num 
    # print(cache_category_name)
    # cached_data = cache.get(cache_category_name)
    # if cached_data:
    #     print('here')
    #     print(cached_data)
    res = Response(cached_data)
    count1 = count if count%2==0 else count+1  # when product list are odd in size add 1 to it so that 
    # get last product . 

    if num>1 and num<=(count1//2):  # 2 only represents no of products shown on each paginated page.       
        next = num + 1
        if next > (count1//2):
            res['next'] = None
        else:
            res['next'] = request.build_absolute_uri+'&page={}'.format(next) # ('?page={}'.format(next))

        prev =  num - 1  
        request.build_absolute_uri()+'?page={}'.format(str(num))#('?page={}'.format(str(num)))
        res['count'] = count
        
        res['previous'] = request.build_absolute_uri()+'&page={}'.format(prev)# ('?page={}'.format(prev))
        # else:
        return res
    else:
        print(12345)
        res['count'] = count
        next = num + 1
        if next > (count1//2):
            res['next'] = None
        else:
            res['next'] = request.build_absolute_uri()+'&page={}'.format(next)# ('?page={}'.format(next))
        res['previous'] = None
        return res



