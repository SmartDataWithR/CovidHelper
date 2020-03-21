from django.urls import path 
from django.conf.urls import url
from .views import HomePageView, AboutPageView, ip, index, change_password

urlpatterns = [
    path('', index, name='home'),
    url(r'^password/$', change_password, name='change_password'),
    #path('', HomePageView.as_view(), name='home'),
    
    path('about/', AboutPageView.as_view(), name='about'),
    path('ip', ip),
]
