from django.urls import path
from . import views


urlpatterns = [
    path('categories/', views.ListCategories.as_view(), name='categories'),
]