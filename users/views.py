from django.shortcuts import render, redirect
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.decorators import login_required, permission_required
from django.db import transaction
import geopy
import pandas as pd

# Create your views here.
@login_required
@transaction.atomic
def updateUser(request):
    user = CustomUser.objects.get(email=request.user)
    # df = pd.DataFrame([u.slogan, u.description, u.email] for u in CustomUser.objects.raw('SELECT * FROM users_customuser') )
    # df.columns = ['slogan', 'description', 'username']
    
    # # find out if user profile is filled
    # df_filt = df[df['username'] == str(request.user)]
    # slogan = df_filt['slogan'][0]
    # description = df_filt['description'][0]
    # if len(slogan)>0 or len(description)>0:
    #     return redirect('/')

    #user = CustomUser.objects.get(id=id)
    locator = geopy.Nominatim(user_agent="myGeocoder")
    form = CustomUserChangeForm(instance=user)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        
        # location = locator.geocode(address)
        if form.is_valid():
            data = request.POST.copy()
            address = data.get('street') + ' ' + data.get('zip_code') + ' ' + data.get('city_name')
            location = locator.geocode(address)
            
            # replace the longitude latitude information
            form_new = form.save(commit=False)
            form_new.longitude = location.longitude
            form_new.latitude = location.latitude
            form_new.save()

            return redirect('/')
        else:
            form = CustomUserChangeForm(request.POST, instance=user)
            print(request.POST)
            context = {'form': form}
    return render(request, 'users/updateUser.html', {'form': form}) 
