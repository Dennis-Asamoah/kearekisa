from unicodedata import category
from django.urls import path
from . import views


urlpatterns = [
    path('categories/', views.ListCategories.as_view(), name='categories'),
    # This url path lists all categories and their associated 
    # subcategories. eg Electronic category lists TV and visuals, phones and tablets etc
    # as subcategories.
    path('categories_and_subcategories', views.ListCategoriesAndItsSubcategories.as_view(),
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
    path('subcategories/<slug:slug>/products', views.RetrieveSubCategoryProducts.as_view(), 
    name='retrieve_subcategory_products'
    ),
    # This url maps to an endpoint that filters according to a particular subcategory.
    # slug represents a a subcategory
    path('subcategories/<slug:slug>/filter', views.FilterProducts.as_view(), name='filter_products'),
    # This url maps to and endpont that lists all products associated with a certain type.
    # Example, a type of apple will lists all iphones 
    path('types/<slug:slug>', views.RetrieveType.as_view(), name='retrieve_type'),
    path('regions/', views.ListRegions.as_view(), name='regions'),
    path('regions/<slug:slug>', views.RetrieveRegion.as_view(), name='retrieve_regions'),
    #
    path('categories/<slug:slug>/products-and-subcategory', 
    views.ListCategoryProductsAndSubcategory.as_view(),
    name='retrieve_products_and_subcategorycategory'
    ),
    # slug represents subcategory
    path('subcategories/<slug:slug>/products-and-types', 
    views.ListSubCategoryProductsAndTypes.as_view(),
    name='retrieve_product_and_type'
    ),
    path('<slug:category_slug>/<slug:subcategory_slug>/<slug:product_slug>',
     views.RetrieveProduct.as_view(), name='product'),
    path('regions1/<slug:slug>', views.Test.as_view(), name='test'),

]