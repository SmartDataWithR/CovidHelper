from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        
        fields = ('email', 'username')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('first_name', 'username', 'street', 'city_name', 'zip_code', 'tel_private', 'tel_mobile', 'web', 'skype', 'linkedin',  'slogan', 'description', 'last_login', 'longitude', 'latitude')#, 'group_membership', ),'registered_on',
