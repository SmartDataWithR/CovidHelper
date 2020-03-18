from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
import requests
import geopy

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        
        fields = ('email', 'username')

class CustomUserChangeForm(UserChangeForm):
    #current_id = 8
    class Meta:

        # locator = geopy.Nominatim(user_agent="myGeocoder")
        
        model = CustomUser  
        # obj = model.objects.get(pk=8) 
        # address = obj.street + ' ' + str(obj.zip_code) + ' ' +obj.city_name
        # location = locator.geocode(address)
        
        # model.objects.filter(pk=8).update(longitude = location.longitude)
        # model.objects.filter(pk=8).update(latitude = location.latitude)
        fields = ('id','first_name','last_name', 'username', 'group_membership', 'help_type', 'street', 'city_name', 'zip_code', 'tel_private', 'tel_mobile', 'web', 'skype', 'linkedin',  'slogan', 'description', 'last_login', 'longitude', 'latitude')#, 'group_membership', ),'registered_on',
