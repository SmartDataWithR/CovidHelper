from django.contrib import admin
from django.urls import path

from .views import contact, successView

urlpatterns = [
    path('contact/', contact, name='contact'),
    path('success/', successView, name='success'),
]
