from django.urls import path

from .views import HomePageView, AboutPageView, ip, index

urlpatterns = [
    path('', index, name='home'),
    #path('', HomePageView.as_view(), name='home'),
    #path('', index, name='index'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('ip', ip),
    #path('', searchLocation, name='search')
]
