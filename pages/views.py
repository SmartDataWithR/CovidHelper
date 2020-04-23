from django.views.generic import TemplateView
from ipware import get_client_ip
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.conf import settings
from .forms import SearchForm
from users.models import CustomUser
import geopy
from geopy.distance import geodesic
import pandas as pd
import json
from django.utils.translation import gettext as _, activate
# required for IP to numeric
import socket
import struct

# import file for ip's to language mapping
df_ip_lang = pd.read_csv('pages/lng_map.csv', names=['ip_from', 'ip_to', 'country_code', 'country_name', 'lang_code'] )

def ip(request):
    ip, is_routable = get_client_ip(request)
    if ip is None:
        ip = "0.0.0.0"
    else:
        if is_routable:
            ipv = "Public"
        else:
            ipv = "Private"
    return (ip, ipv) 

def ip2int(addr):
    return struct.unpack("!I", socket.inet_aton(addr))[0]

def index(request):
    search = request.POST.get('search-field')
    searchCat = request.POST.get('search-catogery')
    locator = geopy.Nominatim(user_agent="myGeocoder")
    gotodiv = False
    
    # From IP to Language
    #--------------------
    request_ip = ip(request)  # get request IP
    
    request_ip_int = ip2int(request_ip[0])  # convert IP to numeric
    
    df_filt = df_ip_lang[df_ip_lang.ip_from <= request_ip_int] # filter data for fetched ip
    range_to_check = df_filt.iloc[-1]
    is_in_range = request_ip_int > range_to_check.ip_from & request_ip_int < range_to_check.ip_to  # check that my IP is in range
    country_code = 'en-us'  # initialise default language
    if is_in_range:  # if an entry is found in dataframe, set this one to country-code
        country_code = range_to_check.lang_code    
    activate(country_code)  # activate the current language code
    current_path = str(request.get_full_path()).strip('/')
    print(current_path)
    # if user selected a language manually, use this one
    if current_path == 'en':
        activate('en-us')
    elif current_path != '':
        activate(current_path)

    context = {}
    if search != None:
        location = locator.geocode(search, timeout=5)
        if not hasattr(location, 'longitude'):
            location = locator.geocode('Hamburg', timeout=5)
            if search != None and searchCat == '4':
                searchCat = 'NOT NULL'
            #query = 'SELECT * FROM users_customuser'
            #if search != None and searchCat == '4':
                #df = pd.DataFrame([u.id, u.group_membership, u.longitude, u.latitude, u.slogan, u.zip_code, u.description, u.map_show_location,  u.username, u.help_type] for u in CustomUser.objects.raw('SELECT * FROM users_customuser') )
                #query = 'SELECT * FROM users_customuser' 
            #else:
                #df = pd.DataFrame([u.id, u.group_membership, u.longitude, u.latitude, u.slogan, u.zip_code, u.description, u.map_show_location,  u.username, u.help_type] for u in CustomUser.objects.raw('SELECT * FROM users_customuser WHERE group_membership = searchCat') )
                #query = 'SELECT * FROM users_customuser WHERE group_membership = '.searchCat 
                #        df = pd.DataFrame([u.id, u.group_membership, u.longitude, u.latitude, u.slogan, u.zip_code, u.description, u.map_show_location,  u.username, u.help_type, u.userImg_Url] for u in CustomUser.objects.raw('SELECT * FROM users_customuser WHERE group_membership IN(SELECT group_membership FROM users_customuser WHERE (%s<>'' AND group_membership IN('0','1','3')) OR (%s<>'' AND group_membership=group_membership))', [searchCat]) )

        #df = pd.DataFrame([u.id, u.group_membership, u.longitude, u.latitude, u.slogan, u.zip_code, u.description, u.map_show_location,  u.username, u.help_type, u.userImg_Url] for u in CustomUser.objects.raw('SELECT * FROM users_customuser WHERE group_membership IN(SELECT group_membership FROM users_customuser WHERE (%s <> NULL AND group_membership IN('0','1','3')) OR (group_membership = group_membership))', [searchCat]) )
        df = pd.DataFrame([u.id, u.group_membership, u.longitude, u.latitude, u.slogan, u.zip_code, u.description, u.map_show_location,  u.username, u.help_type, u.userImg_Url] for u in CustomUser.objects.raw('SELECT * FROM users_customuser WHERE group_membership like %s', [searchCat]) )
        df.columns = ['id','group_membership', 'longitude', 'latitude', 'slogan', 'zip_code', 'description', 'map_show_location', 'username', 'help_type', 'userImg_Url'] # 
        df['distance'] = [geodesic((location.longitude, location.latitude), (x, y)).miles for x,y in zip(df['longitude'], df['latitude'])]
        
        # filter for distance max 20km (12.4miles)
        df_filt = df[df['distance'] < 12.4]
        
    
        # pass the data to the template
        group_membership = df_filt['group_membership'].values.tolist()
        group_membership = [int(x) for x in group_membership]
        help_type = df_filt['help_type'].values.tolist()
        userImg_Url = df_filt['userImg_Url'].values.tolist()
        slogan = df_filt['slogan'].values.tolist()
        shop_type = df_filt['shop_type'].values.tolist()
        description = df_filt['description'].values.tolist() 
        username = df_filt['username'].values.tolist()
        zipcode = df_filt['zip_code'].values.tolist()
        #tel_private = df_filt['tel_private'].values.tolist()
        #tel_mobile = df_filt['tel_mobile'].values.tolist()
        longitudes = df_filt['longitude'].values.tolist()
        latitudes = df_filt['latitude'].values.tolist()
        ids = df_filt['id'].values.tolist()
        map_show_location = df_filt['map_show_location'].values.tolist()
        map_show_location = [int(x) for x in map_show_location]
        rname = list(range(0, len(ids)))
        template_table = list(zip(rname, ids, slogan, description, zipcode))

        gotodiv = 'search'
        context = {'longitude': location.longitude, 'latitude': location.latitude,'id':ids, 'userImg_Url':userImg_Url, 'group_membership': group_membership, 'longitudes': longitudes, 'latitudes': latitudes, 'slogan': slogan, 'description': description, 'gotodiv': gotodiv, 'map_show_location':map_show_location, 'template_table':template_table, 'username':username, 'help_type':help_type}
        
        
    
    return render(request, 'pages/home.html', context)
    
class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

def searchLocation(request):
    form = SearchForm(request)
    print(form)
    if request.method=='POST':
        form = SearchForm(request.POST)
    return render(request, 'pages/home.html', {'form': form})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'account/password_set.html', {
        'form': form
    })

def privacy(request):
    return render(request, 'pages/privacy.html')

def imprint(request):
    return render(request, 'pages/imprint.html')

def terms(request):
    return render(request, 'pages/terms_conditions.html')

def cookie_policy(request):
    return render(request, 'pages/cookie_policy.html')
