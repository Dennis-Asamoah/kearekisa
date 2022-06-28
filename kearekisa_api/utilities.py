from base.models import Type


def product_type(slug):
    item_type = Type.objects.get(slug=slug)
    type_name = item_type.sub_category.category.name
    print(type_name)
    if type_name == 'Pet':
        return item_type.pet_set.all,type_name
    elif type_name == 'Electronics':
        return item_type.electronic_set.all,type_name
