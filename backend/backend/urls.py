"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib.auth import get_user_model
from django.contrib import admin
from django.urls import path
from django.contrib.sitemaps.views import sitemap
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_swagger.views import get_swagger_view
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework.schemas import get_schema_view
from rest_framework.routers import DefaultRouter
from rest_framework import viewsets, routers
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token
from rest_framework import serializers
from rest_framework import generics
from users.views import AddressViewSet
from users.views import ContactViewSet 
from users.views import TestimonialViewSet
from users.views import AboutUsViewSet
#from users.views import UserViewSet
from users.views import TeamMemberViewSet
from users.views import StateProvinceViewSet
from users.views import ProfileViewSet
User = get_user_model()

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

admin.autodiscover()
router = DefaultRouter()
router.register(r'users',  UserViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'testimonials',  TestimonialViewSet)
router.register(r'aboutus', AboutUsViewSet)
router.register(r'teammembers', TeamMemberViewSet)
router.register(r'states', StateProvinceViewSet)
router.register(r'profiles',  ProfileViewSet)

urlpatterns = [
    path('/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('admin/', admin.site.urls), # admin site
    path('api-auth/', include('rest_framework.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:     
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)     
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
