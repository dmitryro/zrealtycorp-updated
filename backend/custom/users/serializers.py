from .models import Profile
from .models import Testimonial
from .models import Contact
from .models import AboutUs
from .models import TeamMember
from .models import StateProvince
from .models import Address

from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework import generics


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','first_name','last_name', 'email',)

class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ('id', 'title', 'subtitle', 'body',)

class StateProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateProvince
        fields = ('id','name','abbreviation')   

class AddressSerializer(serializers.ModelSerializer):
    state = StateProvinceSerializer(many=False,read_only=True)
    class Meta:
        model = Address
        fields = ('id','state','address1','address2','city','postal_zip','country')

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id','name', 'time_contacted', 'subject', 'phone', 'email', 'message')

class TeamMemberSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    class Meta:
        model = TeamMember
        fields = ('id', 'user', 'username', 'first_name', 'last_name', 'title', 'bio', 'avatar')

class ProfileSerializer(serializers.ModelSerializer):
    #   user = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Profile
        fields = ('id','username','user','email','first_name','last_name','date_joined','is_new','phone')

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ('id', 'username', 'first_name', 'last_name', 'user', 'phone', 'email', 'link_title', 'link', 'body',)
