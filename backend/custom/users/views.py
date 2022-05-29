from django.shortcuts import render
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
import logging
from rest_framework import filters
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import viewsets

#from django.contrib.auth.models import User
from .models import User
from .models import Profile
from .models import Testimonial
from .models import Contact
from .models import AboutUs
from .models import TeamMember
from .models import StateProvince
from .models import Address

from .serializers import AddressSerializer
from .serializers import ContactSerializer
from .serializers import TestimonialSerializer
from .serializers import AboutUsSerializer
from .serializers import UserSerializer
from .serializers import TeamMemberSerializer
from .serializers import StateProvinceSerializer
from .serializers import ProfileSerializer
# Create your views here.

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# ViewSets define the view behavior.
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_fields = ('id', 'username', 'first_name', 'last_name', 'is_authenticated', 'user',
                     'email', 'is_activated', 'is_new','is_client', 'is_company')


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    filter_fields = ('id','state','address1','address2','city','postal_zip','country',)


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filter_fields = ('id','name', 'time_contacted', 'subject', 'phone', 'email', 'message')


class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    filter_fields = ('id', 'username', 'first_name', 'last_name', 'user', 'phone', 'email', 'link_title', 'link', 'body', 'admin_thumbnail')



class AboutUsViewSet(viewsets.ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class =  AboutUsSerializer
    filter_fields = ('id', 'title', 'subtitle', 'body',)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_fields =  ('id','username','first_name','last_name', 'email',)


class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
    filter_fields =  ('id', 'user', 'username', 'first_name', 'last_name', 'title', 'bio', 'avatar')

   
class StateProvinceViewSet(viewsets.ModelViewSet):
    queryset = StateProvince.objects.all()
    serializer_class = StateProvinceSerializer
    filter_fileds = ('id','name','abbreviation') 
