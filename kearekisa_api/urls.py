from unicodedata import category
from django.urls import path
from . import views


urlpatterns = [
    path('categories/', views.ListCategories.as_view(), name='categories'),
    path('categories/<slug:slug>',views.RetrieveCategory.as_view(), name='retrieve_category'),
    path('categories/<slug:slug>/products', views.ListCategoryProducts.as_view(), name='retrieve_category_produtcs'),
    path('subcategories/<slug:slug>', views.RetrieveSubCategory.as_view(), name='retrieve_subcategory'),
    path('subcategories/<slug:slug>/products', views.RetrieveSubCategoryProducts.as_view(), 
    name='retrieve_subcategory_products'
    ),
    path('subcategories/<slug:slug>/filter', views.FilterProducts.as_view(), name='filter_products'),
    path('types/<slug:slug>', views.RetrieveType.as_view(), name='retrieve_type'),
    path('regions/', views.ListRegions.as_view(), name='regions'),
    path('regions/<slug:slug>', views.RetrieveRegion.as_view(), name='retrieve_regions'),
    path('categories/<slug:slug>/products-and-subcategory', 
    views.ListCategoryProductsAndSubcategory.as_view(),
    name='retrieve_products_and_subcategorycategory'
    ),
    path('subcategories/<slug:slug>/products-and-types', 
    views.ListSubCategoryProductsAndTypes.as_view(),
    name='retrieve_product_and_type'
    ),
    path('regions1/<slug:slug>', views.Test.as_view(), name='test'),

]