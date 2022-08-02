from django.apps import AppConfig
from django.db.models.signals import  pre_save, post_save, pre_delete, post_delete

# from kearekisa_api.utilities import subcategory_product
from .signals import * 


class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'

    def ready(self):
        category_model = self.get_model('Category')
        electronic_category_model = self.get_model('Electronic')
        # NB: DO SAME FOR THE REST OF THE CATEGORIES
        subcategory_model = self.get_model('SubCategory')
        type_model = self.get_model('Type')
        pre_save.connect(update_cache_for_listcategories, sender=category_model)
        # pre_save.connect(update_cache_listcategoryproducts_electronics, sender=electronic_category_model)
        post_save.connect(update_cache_list_category_and_its_subcategories, sender=subcategory_model)
        pre_save.connect(update_cache_for_retrieve_subcategories_of_categories_view, sender=subcategory_model)
        pre_save.connect(update_cache_for_retrieve_types_of_subcategories_view, sender=type_model)
        pre_save.connect(update_cache_for_list_subcategories_products_view, sender=electronic_category_model)


