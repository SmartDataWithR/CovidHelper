from django.urls import path 
from django.conf.urls import url
from .views import HomePageView, AboutPageView, ip, index, change_password, privacy, imprint, terms, cookie_policy

urlpatterns = [
    path('', index, name='home'),
    url(r'^password/$', change_password, name='change_password'),
    #path('', HomePageView.as_view(), name='home'),
    
    path('about/', AboutPageView.as_view(), name='about'),
    path('privacy', privacy, name='privacy'),
    path('imprint', imprint, name='imprint'),
    path('terms', terms, name='terms'),
    path('cookie_policy', cookie_policy, name='cookie_policy'),    
    path('ip', ip),
]
