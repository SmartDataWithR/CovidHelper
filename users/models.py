from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime


class CustomUser(AbstractUser):
    GROUPS = (
        (0, 'helper'),
        (1, 'taker')
    )
    group_membership = models.CharField(max_length=1, choices=GROUPS, default=1)
    street = models.CharField(max_length=100, blank=True)
    city_name = models.CharField(max_length=100, blank=True)
    zip_code = models.IntegerField(blank=True, default=0)
    longitude = models.FloatField(default=10)
    latitude = models.FloatField(default=52)
    tel_private = models.CharField(max_length=100, blank=True)
    tel_mobile = models.CharField(max_length=100, blank=True)
    web = models.CharField(max_length=100, blank=True)
    skype = models.CharField(max_length=100, blank=True)
    linkedin = models.CharField(max_length=100, blank=True)
    profile_image = models.ImageField(upload_to='profile_image', blank=True)
    registered_on = models.DateTimeField(blank=True, null=True)  # sets the value whenever created
    last_login = models.DateTimeField(blank=True, null=True)  # updates whenever last accessed
    slogan = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=100, blank=True)



    def __str__(self):
        return self.email