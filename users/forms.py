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
    
    class Meta:
        model = CustomUser  
        fields = ('id', 'username', 'group_membership','map_show_location', 'street', 'city_name', 'zip_code', 'slogan', 'description')# , 'longitude', 'latitude')
