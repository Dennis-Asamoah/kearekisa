"""kearekisa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view



urlpatterns = [
    path('auth/', include('drf_social_oauth2.urls', namespace='drf')),
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('api/v1/', include('kearekisa_api.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
    path('doc/', include_docs_urls(title='kearekisa_api')),
    path('schema/', get_schema_view(
        title='kearekisa_api_schema',
        description='kearekisa_schema_api',
        version='1.0.0'
    ), name='open_core_api'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
    )
