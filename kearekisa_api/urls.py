from unicodedata import category
from django.urls import path
from . import views


urlpatterns = [
    path('categories/', views.ListCategories.as_view(), name='categories'),
    # This url path lists all categories and their associated 
    # subcategories. eg Electronic category lists TV and visuals, phones and tablets etc
    # as subcategories.
    path('categories-and-subcategories', views.ListCategoriesAndItsSubcategories.as_view(),
     name='categories_and_its_subcategories'),
    # This url path lists the subcategories of a particlar category 
    # the slug represents the category eg electronic category.
    # So the path 'categories/electronics' will list TV and visual and 
    # the rest of the its subcategories.  
    path('categories/<slug:slug>',views.RetrieveSubcategoriesOfCategory.as_view(),
     name='retrieve_category'),
    # lists all products associated with a category irrespective of subcategory or type.
    # eg samsung phone and samsung flatscreen are both under 'electronics product'
    # but are under different subcategories. The 'slug' represents a particular category eg Vehicle,Pet 
    path('categories/<slug:slug>/products', views.ListCategoryProducts.as_view(),
     name='retrieve_category_produtcs'),
    # this endpoint lists all the types associated with a  partticular
    # subcategory. eg the subcategory 'phones and tablets' will list 
    # 'Apple','samsung phone and tablets'. 
    path('subcategories/<slug:slug>', views.RetrieveTypesOfSubCategory.as_view(), 
    name='retrieve_subcategory'),
    # This path maps to an endpoint that lists all products under
    # a particular subcategory eg Under 'phones and tablets' will print 
    # all phones and tablest(apple, samsung etc)
    # NB: the slug represents a subcategory eg phones-and-tablets 
    path('subcategories/<slug:slug>/products', views.ListSubCategoryProducts.as_view(), 
    name='list_subcategory_products'
    ),
    # This url maps to an endpoint that filters according to a particular subcategory.
    # slug represents a a subcategory
    path('subcategories/<slug:slug>/filter', views.FilterProducts.as_view(), name='filter_products'),
    # This url maps to and endpont that lists all products associated with a certain type.
    # Example, a type of apple will lists all iphones 
    # slug represents type
    path('types/<slug:slug>', views.ListType.as_view(), name='list_type'),
    path('regions/', views.ListRegions.as_view(), name='regions'),
    path('regions/<slug:slug>', views.ListSubregions.as_view(), name='list_subregions'),
    # This url links to an enpdpint that lists all the products in a category and 
    # their subcategory. eg Electronic category  will list [samsumg phone, iphone etc, tvs etc]  
    #  together with their subcategory ie ['tv and visuals', etc]
    # slug repressents a category eg Electronic, Property  
    path('categories/<slug:slug>/products-and-subcategory', 
    views.ListCategoryProductsAndSubcategory.as_view(),
    name='retrieve_products_and_subcategorycategory'
    ),
    # This url maps to an endpoint thats lists all the products associated with  a particular 
    # subcategory. It also lists the types associated with this particular subcategory .
    # slug represents subcategory
    path('subcategories/<slug:slug>/products-and-types', 
    views.ListSubCategoryProductsAndTypes.as_view(),
    name='retrieve_product_and_type'
    ),
    # This url maps to an endpoint that lists the details of a product together with 
    # similar products.
    # category_slug represents category, subcategory_slug represents subcategory
    # and product_slug represents product.
    path('<slug:category_slug>/<slug:subcategory_slug>/<slug:product_slug>',
     views.RetrieveProduct.as_view(), name='product'),
    path('regions1/<slug:slug>', views.Test.as_view(), name='test'),
    path('produce/', views.CeleryProducer.as_view(), name='producer'),
    path('consume/<str:id>', views.CeleryConsumer.as_view(), name='consumer'),


]