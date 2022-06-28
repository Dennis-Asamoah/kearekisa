from unicodedata import category
from django.urls import path
from . import views


urlpatterns = [
    path('categories/', views.ListCategories.as_view(), name='categories'),
    path('categories/<slug:slug>',views.RetrieveCategory.as_view(), name='retrieve_category'),
    path('subcategories/<slug:slug>', views.RetrieveSubCategory.as_view(), name='retrieve_subcategory'),
    path('types/<slug:slug>', views.RetrieveType.as_view(), name='retrieve_type'),
    path('regions/', views.ListRegions.as_view(), name='regions'),
    path('regions/<slug:slug>', views.RetrieveRegion.as_view(), name='retrieve_regions'),
    path('regions1/<slug:slug>', views.Test.as_view(), name='test'),

]