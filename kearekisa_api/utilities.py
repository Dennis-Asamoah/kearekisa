from base.models import Type
from base.models import SubCategory

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

