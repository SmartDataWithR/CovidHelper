from django.shortcuts import render, redirect
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomShopChangeForm
from django.contrib.auth.decorators import login_required, permission_required
from django.db import transaction
import geopy
import pandas as pd

@login_required
@transaction.atomic
# check if there is a text in "description"
# yes: redirect to /
# no: redirect to /update
def redirect_select(request):
    user = CustomUser.objects.get(email=request.user)
    df = pd.DataFrame([u.description, u.email, u.group_membership] for u in CustomUser.objects.raw('SELECT * FROM users_customuser') )
    df.columns = ['description', 'username', 'group_membership']
    print(df)
    # find out if user profile is filled
    df_filt = df[df['username'] == str(request.user)]
    # slogan = df_filt['slogan'][0]
    description = df_filt.iloc[0,0]
    group_membership = df_filt.iloc[0,2]

    if description==None:
        desc_length=0
    else:
        desc_length=len(description)
    
    if desc_length>0:
        return redirect('/')
    else:
        if group_membership == '3':
            return redirect('/updateShop/')
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

@login_required
@transaction.atomic
def updateShop(request):
    
    user = CustomUser.objects.get(email=request.user)
    locator = geopy.Nominatim(user_agent="myGeocoder")
    form = CustomShopChangeForm(instance=user)
    
    if request.method == 'POST':
        form = CustomShopChangeForm(request.POST,request.FILES, instance=user)
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
            form_new.group_membership = '3'
            if form.is_valid() and 'user_Main_Img' in request.FILES:
                Imagename = request.FILES['user_Main_Img'].name
                form_new.userImg_Url = Imagename
                form_new.save()
                return redirect('/')
            else:
                form_new.save()
                return redirect('/')
        else:
            form = CustomShopChangeForm(request.POST, instance=user)
            context = {'form': form}
    return render(request, 'users/updateShop.html', {'form': form}) 
