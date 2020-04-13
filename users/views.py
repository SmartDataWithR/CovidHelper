from django.shortcuts import render, redirect
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.decorators import login_required, permission_required
from django.db import transaction
import geopy
import pandas as pd

@login_required
@transaction.atomic
def redirect_select(request):
    user = CustomUser.objects.get(email=request.user)
    df = pd.DataFrame([u.description, u.email] for u in CustomUser.objects.raw('SELECT * FROM users_customuser') )
    df.columns = ['description', 'username']
    
    # find out if user profile is filled
    df_filt = df[df['username'] == str(request.user)]
    # slogan = df_filt['slogan'][0]
    description = df_filt.iloc[0,0]
    # slogan_length=len(slogan)
    desc_length=len(description)
    
    if desc_length>0:
        return redirect('/')
    else:
        return redirect('/update/')

# Create your views here.
@login_required
@transaction.atomic
def updateUser(request):
    user = CustomUser.objects.get(email=request.user)

    #user = CustomUser.objects.get(id=id)
    locator = geopy.Nominatim(user_agent="myGeocoder")
    form = CustomUserChangeForm(instance=user)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST,request.FILES, instance=user)
        # location = locator.geocode(address)
        if form.is_valid():
            data = request.POST.copy()
            
            address = data.get('street') + ' ' + data.get('zip_code') + ' ' + data.get('city_name')
            location = locator.geocode(address)
            #Imagename = request.FILES['user_Main_Img'].name
            # replace the longitude latitude information
            form_new = form.save(commit=False)
            form_new.longitude = location.longitude
            form_new.latitude = location.latitude
            if form.is_valid() and 'user_Main_Img' in request.FILES:
                Imagename = request.FILES['user_Main_Img'].name
                form_new.userImg_Url = Imagename
                form_new.save()
                return redirect('/')
            else:
                form_new.save()
                return redirect('/')
        else:
            form = CustomUserChangeForm(request.POST, instance=user)
            context = {'form': form}
    return render(request, 'users/updateUser.html', {'form': form}) 
