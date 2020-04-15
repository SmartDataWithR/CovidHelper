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
    city_name = forms.CharField(required=False, widget= forms.TextInput(attrs={'placeholder':'your city'}))
    zip_code = forms.CharField(required=False, widget= forms.TextInput(attrs={'placeholder':'zip-code'}))
    street = forms.CharField(required=False, widget= forms.TextInput(attrs={'placeholder':'your street (max. characters 500)'}))
    slogan = forms.CharField(required=False, widget= forms.TextInput(attrs={'placeholder':'Describe yourself or the type of help'}))
    description = forms.CharField(required=False, widget= forms.TextInput(attrs={'placeholder':'Please add more specific information'}))
    class Meta:
        model = CustomUser  
        fields = ('id', 'group_membership', 'help_type','street', 'city_name', 'zip_code', 'slogan', 'description', 'user_Main_Img', 'userImg_Url')# , 'longitude', 'latitude')
