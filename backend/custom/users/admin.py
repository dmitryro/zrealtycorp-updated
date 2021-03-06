from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from imagekit.admin import AdminThumbnail
from .models import Profile
from .models import Testimonial
from .models import Contact
from .models import AboutUs
from .models import TeamMember
from .models import StateProvince
from .models import Address
# Register your models here.
########################################
#  Register Profile with Django Admin  #
########################################

class ProfileAdmin(admin.ModelAdmin):
    fieldsets = ((None, {'fields': ['username',
                                    'email', 
                                    'user',
                                    'is_cleared',
                                    'is_activated',
                                    'is_facebook_signup_used',
                                    'is_google_signup_used',
                                    'is_linkedin_signup_used',
                                    'is_username_customized',
                                    'is_twitter_signup_used',
                                    'is_new',
                                    'first_name','last_name',
                                    'phone','address',
                                    'profile_image_path']}),)

    list_display = ('id','username','user','email','first_name','last_name','date_joined','is_new','phone')

    list_editable = ('username','user','email','first_name','last_name','is_new','phone',)
    search_fields = ('username', 'first_name', 'last_name','email','phone',)

    class Meta:
         verbose_name = 'User Profile'
         verbose_name_plural = 'User Profiles'


class AddressAdmin(admin.ModelAdmin):
    fieldsets = ((None, {'fields': ['address1',
                                    'address2',
                                    'city',
                                    'state_province',
                                    'country',
                                    'postal_zip']}),)
    list_display = ('id','address1','address2', 'city', 'state_province','country','postal_zip',)
    list_editable = ('address1','address2', 'city', 'state_province','country','postal_zip',)
    search_fields = ('address1','address2', 'city', 'state_province','country','postal_zip',)


    class Meta:
         verbose_name = 'Address'
         verbose_name_plural = 'Addresses'


class StateProvinceAdmin(admin.ModelAdmin):

    fieldsets = ((None, {'fields': ['abbreviation','name',]}),)
    list_display = ('id', 'abbreviation', 'name',)
    list_editable = ('abbreviation','name',)


class CustomUserAdmin(UserAdmin):
    def __init__(self, *args, **kwargs):
        super(UserAdmin,self).__init__(*args, **kwargs)
        UserAdmin.list_display = list(UserAdmin.list_display) + ['id','date_joined', 'last_login','is_active']

    # Function to count objects of each user from another Model (where user is FK)
    def some_function(self, obj):
        return obj.another_model_set.count()


class TestimonialAdmin(admin.ModelAdmin):
    bio = forms.CharField( widget=forms.Textarea )
    fieldsets = [
      ('Body', {'classes': ('full-width',), 'fields': ('username','first_name','last_name','user','phone','email', 'link_title', 'link', 'body','avatar')})
    ]
    list_display = ('__str__', 'username', 'first_name', 'last_name', 'user', 'phone', 'email', 'link_title', 'link', 'body',)
    admin_thumbnail = AdminThumbnail(image_field='avatar_thumbnail')
    search_fields = ('username', 'first_name', 'last_name', 'user', 'phone', 'email', 'link_title', 'link', 'body')

    class Meta:
         verbose_name = 'Testimonial'
         verbose_name_plural = 'Testimonials'


class ContactAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'id', 'name', 'phone', 'email', 'message')
    search_fields = ('id', 'name', 'phone', 'email', 'message')

    class Meta:
         verbose_name = 'Contact'
         verbose_name_plural = 'Contacts'


class AboutUsAdmin(admin.ModelAdmin):
    body = forms.CharField( widget=forms.Textarea )
    fieldsets = [
      ('Body', {'classes': ('full-width',), 'fields': ('title','subtitle','body','avatar')})
    ]
    list_display = ('__str__','title','subtitle','body',)
    admin_thumbnail = AdminThumbnail(image_field='avatar_thumbnail')


class TeamMemberAdmin(admin.ModelAdmin):
    bio = forms.CharField( widget=forms.Textarea )
    fieldsets = [
      ('Body', {'classes': ('full-width',), 'fields': ('username','first_name','last_name','is_associate','is_partner','phone','email','title','bio','avatar')})
    ]
    list_display = ('__str__','first_name','last_name','is_partner','is_associate','phone','email','title','bio', 'admin_thumbnail')
    admin_thumbnail = AdminThumbnail(image_field='avatar_thumbnail')
    search_fields = ('username', 'first_name', 'last_name','email','phone','title')


admin.site.register(StateProvince, StateProvinceAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(Address, AddressAdmin);
#admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
#admin.site.unregister(Group)
