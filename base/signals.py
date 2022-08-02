from pickletools import optimize
from django.core.cache import cache
from collections import OrderedDict
from os.path import join
from random  import  randint


# loading from files doesn't work for some reasons
# from kearekisa_api.utilities import post_product 


def update_cache_for_listcategories(sender, instance, **kwargs):
    # from .serializers import CategorySerializer #  does work if place on top
    cache_name = 'list_all_categories'
    data = cache.get(cache_name)
    make_od = OrderedDict() # od=> ordered_dict
    make_od['name'] = instance.name
    make_od['slug'] = instance.slug
    data.append(make_od)   
    print (data)
    cache.set(cache_name, data, None)
    print(make_od)
    raise (10)
    
    # Thinking about upadting 'categories_and_its_subcategories_data' cache
    # from .models import Category
    # from .serializers import  CategoryAndItsSubcategoriesSeriaizer
    # queryset = Category.objects.all()
    # optimized_queryset = CategoryAndItsSubcategoriesSeriaizer.setup_eager_loading(queryset)
    # serializer = CategoryAndItsSubcategoriesSeriaizer(optimized_queryset, many=True)
    # cache.set('categories_and_its_subcategories_data', serializer.data, None)
    # print('done')     

# def update_cache_listcategoryproducts_electronics(sender, instance, **kwargs):
#     print(65)
#     cache_name = 'list_of_electronics_products'
#     data = cache.get(cache_name)

#     ##### start of processing image path #####
#     image_list = [] 
#     print(instance.image_urls)
#     x = instance.image_urls
#     x = x.split('-')
#     # x = [join('/media/electronic', i ) for i in x]
#     x = ['/media/electronic/{}'.format(i)  for i in x]
#     for i in x: 
#         image = OrderedDict()
#         image['id'] = randint(1000,5000)
#         image['image'] = i
#         image_list.append(image)
#     ####### end of image path ############
    
#     make_od = OrderedDict()
#     make_od['electronic_image'] = image_list
#     make_od['name'] = instance.name
#     make_od['description'] = instance.description
#     make_od['price'] = instance.price
#     make_od['slug'] = instance.slug
#     make_od['electronic_model'] = instance.electronic_model
#     make_od['condition'] = instance.condition

#     ####  postered by ###########
#     x = OrderedDict()
#     x['name'] = instance.postered_by.name
#     x['email'] = instance.postered_by.email 
#     make_od['postered_by'] = x

#     ######## end subcategory ###############
    
#     #####  subcategory ########
#     sub = OrderedDict()
#     sub['id'] = randint(1,10)
#     sub_c = OrderedDict()
#     sub_c['id'] = randint(1, 10)
#     sub_c['name'] = instance.subcategory.category.name
#     sub_c['date'] = None
#     sub['category'] = sub_c
#     make_od['subcategory'] = sub
#     ###### end subcategory ############
#     print(instance.type)
#     make_od['type'] = None #  make_od['type'] = instance.type.id
#     make_od['subregion'] = instance.subregion.id  # only instance.subregion will throew error
     
#     print(make_od)
#     data.append(make_od) 
#     # data.pop()
#     cache.set(cache_name, data, None)
#     raise (20)
# NB: DO SAME THING FOR THE REST OF THE CATEGORIES

# def update_cache_listcategoryproducts_electronics(sender, instance, **kwargs):
#     from kearekisa_api.utilities import post_product

def update_cache_list_category_and_its_subcategories(sender, instance, created, **kwargs):
    if created:
        # This is only triggered by the admins
        from .models import Category
        from .serializers import  CategoryAndItsSubcategoriesSeriaizer
        
        queryset = Category.objects.all()
        optimized_queryset = CategoryAndItsSubcategoriesSeriaizer.setup_eager_loading(queryset)
        serializer = CategoryAndItsSubcategoriesSeriaizer(optimized_queryset, many=True)
        cache.set('categories_and_its_subcategories_data', serializer.data, None)
        print('done')
        # raise(12)        
        # Thinking about updating 'categories_and_its_subcategories_data' cache
        # from the update_cache_for_listcategories(sender, instance, **kwargs).
        # Also thing about  append staright into the ordered list instead of fetching from db 


def update_cache_for_retrieve_subcategories_of_categories_view(sender, instance, **kwargs):
    make_ordered_dict = OrderedDict()
    category_ordered_dict = OrderedDict()
    category_ordered_dict['name'] = instance.category.name
    category_ordered_dict['slug'] = instance.category.slug
    make_ordered_dict['category'] = category_ordered_dict
    make_ordered_dict['name'] = instance.name
    make_ordered_dict['slug'] = instance.slug

    slug = category_ordered_dict['slug']
    cache_name = 'retrieve_subcategory_of_' + slug
    
    cached_data = cache.get(cache_name) # a list of ordereddisct
    cached_data.append(make_ordered_dict)
    # cached_data.pop()
    cache.set(cache_name, cached_data, None)
    print('cool')

    print(cached_data)
    # raise (10)
    # NB: Works for all the categories 

def update_cache_for_retrieve_types_of_subcategories_view(sender, instance, **kwargs):
    make_ordered_dict = OrderedDict()
    make_ordered_dict['type_name'] = instance.type_name
    make_ordered_dict['slug'] = instance.slug
    make_ordered_dict['sub_category'] = instance.sub_category.id
    slug = instance.sub_category.slug
    cache_name = 'retrieve_types_of_' + slug
    cached_data = cache.get(cache_name)
    cached_data.append(make_ordered_dict)
    cache.set(cache_name, cached_data, None)
    print('good stuff')

def update_cache_for_list_subcategories_products_view(sender, instance, **kwargs):
    # print(65)
    # cache_name = 'list_of_electronics_products'
    # data = cache.get(cache_name)

    ##### start of processing image path #####
    image_list = [] 
    print(instance.image_urls)
    x = instance.image_urls
    x = x.split('-')
    # x = [join('/media/electronic', i ) for i in x]
    x = ['/media/electronic/{}'.format(i)  for i in x]
    for i in x: 
        image = OrderedDict()
        image['id'] = randint(1000,5000)
        image['image'] = i
        image_list.append(image)
    ####### end of image path ############
    
    make_od = OrderedDict()
    make_od['electronic_image'] = image_list
    make_od['name'] = instance.name
    make_od['description'] = instance.description
    make_od['price'] = instance.price
    make_od['slug'] = instance.slug
    make_od['electronic_model'] = instance.electronic_model
    make_od['condition'] = instance.condition

    ####  postered by ###########
    x = OrderedDict()
    x['name'] = instance.postered_by.name
    x['email'] = instance.postered_by.email 
    make_od['postered_by'] = x

    ######## end subcategory ###############
    
    #####  subcategory ########
    sub = OrderedDict()
    sub['id'] = randint(1,10)
    sub_c = OrderedDict()
    sub_c['id'] = randint(1, 10)
    sub_c['name'] = instance.subcategory.category.name
    sub_c['date'] = None
    sub['category'] = sub_c
    make_od['subcategory'] = sub
    ###### end subcategory ############
    # print(instance.type)
    make_od['type'] = None #  make_od['type'] = instance.type.id
    make_od['subregion'] = instance.subregion.id # only instance.subregion will throew error
    
    slug = instance.subcategory.slug
    slug2 = instance.type.slug
    slug3 = instance.subcategory.category.slug
    # print(slug2.type_name, slug2.slug, slug2.sub_category.name)
    cache_name = 'list_' + slug + '_products'
    cache_name2 = 'retrieve_'+'type_'+ slug2
    cache_name3 = 'list_' + slug + '_products_and_types'
    cache_name4 = 'list_' + slug3 + '_products_and_its_subcategories'
    # print(cache_name2)
    # data = cache.get(cache_name)
    data = cache.get_many([cache_name, cache_name2, cache_name3, cache_name4])
    # print(make_od)
    # print(data[cache_name])
    # print('*********************************')
    # print(data[cache_name2])
    data1 = data[cache_name]
    data2 = data[cache_name2]
    data3 = data[cache_name3]  # a dictionary is produced 
    data3_a = data3['category_product']  # a list is produced
    data4 =  data[cache_name4]
    data4_a = data4['category_product']
    # print(data3['category_product'])
    print(data4)
    ## data1.append(make_od)
    ## data2.append(make_od)
    # data3_a.append(make_od)
    data4_a.append(make_od)
    print('********')
    ## print(data1)
    ## print(data2)
    # print(data3['category_product'])
    print('********')
    # print(data3)
    # print(type(data))
    ## data.append(make_od) 
    # data.pop()
    # data.pop()
    # #print(45)
    # #print(data)
    # #cache.set(cache_name, data, None)
    cache.set_many({cache_name: data1, cache_name2: data2, cache_name3: data3, cache_name4: data4}, None)
    raise (20)
# NB: DO SAME THING FOR THE REST OF THE CATEGORIES
 
