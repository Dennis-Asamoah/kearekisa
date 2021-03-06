# from base.models import Category, Electronic, Type
# from base.models import SubCategory
from collections import namedtuple
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
    item_type = Type.objects.get(slug=slug)
    type_name = item_type.sub_category.category.name
    print(type_name)
    if type_name == 'Pet':
        return item_type.pet_set.all,type_name
    elif type_name == 'Electronics':
        return item_type.electronic_set.all,type_name

def  subcategory_product(slug):
    subcategory = SubCategory.objects.get(slug=slug)
    category_name = subcategory.category.name
    if slug in electronic_subcategories:
        print(subcategory.name)
        print(subcategory.type_set.all())
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
    category = Category.objects.get(slug=slug)
    category_name = category.name
    if category_name == 'Electronics':
        return Electronic.objects.all(), category.subcategory.all(), category_name
    elif category_name == 'Pet':
        return Pet.objects.all(), category.subcategory.all(), category_name
    # do not forget to do it for the rest of the categories 

def subcategory_product_and_types(slug):
    subcategory = SubCategory.objects.get(slug=slug)
    if slug in electronic_subcategories:
        return subcategory.electronic_set.all(), subcategory.type_set.all(), subcategory.category.name
    elif slug in pet_subcategories:
        return subcategory.pet_set.all(), subcategory.type_set.all(), subcategory.category.name

    # do not forget to do it for the rest of the categories

def product_and_related_prouducts(category_slug, product_slug):
    category = Category.objects.get(slug=category_slug)
    category_name = category.name
    if category.name == 'Electronics':
        product = Electronic.objects.get(slug=product_slug)
        related_products  =Electronic.objects.exclude(slug=product_slug)
        return product, related_products, category_name 
    elif category.name == 'Pets':
        product = Pet.objects.get(slug=product_slug)
        related_products  =Pet.objects.get(slug=product_slug)
        return product, related_products, category_name 
    # DO it for the rest  of the categories 

# This function is responsible for publishin new items.
def post_product(request, slug):
    data = request.POST
    images = request.FILES.getlist('images')
    print(images)
    category = Category.objects.get(slug=slug)
    category_name = category.name
    if category.name == 'Electronics':
        # let save the data in the serialiser
        serializer = ElectronicSerializer(data=data)
        if serializer.is_valid():
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



