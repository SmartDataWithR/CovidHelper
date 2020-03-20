from django.views.generic import TemplateView
from ipware import get_client_ip
from django.shortcuts import render
from .forms import SearchForm
from users.models import CustomUser
import geopy
from geopy.distance import geodesic
import pandas as pd
import json

def index(request):
    search = request.POST.get('search-field')
    locator = geopy.Nominatim(user_agent="myGeocoder")
    context = {}
    if search != None:
        location = locator.geocode(search)
        # for u in CustomUser.objects.raw('SELECT * FROM users_customuser'):
        #     print(u.longitude)
        df = pd.DataFrame([u.first_name, u.last_name, u.group_membership, u.help_type, u.longitude, u.latitude, u.tel_private, u.tel_mobile, u.web, u.slogan, u.description] for u in CustomUser.objects.raw('SELECT * FROM users_customuser') )
        df.columns = ['first_name', 'last_name', 'group_membership', 'help_type', 'longitude', 'latitude', 'tel_private', 'tel_mobile', 'web', 'slogan', 'description']
        df['distance'] = [geodesic((location.longitude, location.latitude), (x, y)).miles for x,y in zip(df['longitude'], df['latitude'])]
        df_filt = df[df.distance < 400]

        # pass the data to the template
        group_membership = df_filt['group_membership'].values.tolist()
        group_membership = [int(x) for x in group_membership]
        slogan = df_filt['slogan'].values.tolist()
        description = df_filt['description'].values.tolist()
        tel_private = df_filt['tel_private'].values.tolist()
        tel_mobile = df_filt['tel_mobile'].values.tolist()
        longitudes = df_filt['longitude'].values.tolist()
        latitudes = df_filt['latitude'].values.tolist()
        print(tel_mobile)
        context = {'longitude': location.longitude, 'latitude': location.latitude, 'group_membership': group_membership, 'longitudes': longitudes, 'latitudes': latitudes, 'slogan': slogan, 'description': description, 'tel_private': tel_private, 'tel_mobile': tel_mobile}
    
    return render(request, 'pages/home.html', context)
    
class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

def ip(request):
    ip, is_routable = get_client_ip(request)
    if ip is None:
        ip = "0.0.0.0"
    else:
        if is_routable:
            ipv = "Public"
        else:
            ipv = "Private"
    print(ip, ipv)
    return render(request, 'pages/home.html')

def searchLocation(request):
    form = SearchForm(request)
    print(form)
    if request.method=='POST':
        form = SearchForm(request.POST)
    return render(request, 'pages/home.html', {'form': form})
