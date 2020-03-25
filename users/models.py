from django.contrib.auth.models import AbstractUser
from django.db import models
from django_google_maps import fields as map_fields

class CustomUser(AbstractUser):
    GROUPS = (
        ('0', 'I want to help'),
        ('1', 'I need help'),
        ('2', 'Inactive (invisible to others)')
    )

    HELP_GROUPS = (
        ('0', 'Delivering Food/Supplies'),
        ('1', 'Medical Aid'),
        ('2', 'Online-Teaching of Students'),
        ('3', 'Child Care'),
        ('4', 'Physical Work'),
    )

    MAP_VIEW = (
        ('0', 'rough'),
        ('1', 'exact')
    )

    group_membership = models.CharField(max_length=1, choices=GROUPS, default=2)
    map_show_location = models.CharField(max_length=1, choices=MAP_VIEW, default=0)
    #help_type = models.CharField(max_length=1, choices=HELP_GROUPS, default=1)
    street = models.CharField(max_length=100, blank=True)
    city_name = models.CharField(max_length=100, blank=True)
    zip_code = models.IntegerField(blank=True, default=0)
    longitude = models.FloatField(default=42, blank=True, null=True)
    latitude = models.FloatField(default=52, blank=True, null=True)
    #tel_private = models.CharField(max_length=100, blank=True)
    #tel_mobile = models.CharField(max_length=100, blank=True)
    #web = models.CharField(max_length=100, blank=True)
    #skype = models.CharField(max_length=100, blank=True)
    #linkedin = models.CharField(max_length=100, blank=True)
    #profile_image = models.ImageField(upload_to='profile_image', blank=True)
    #registered_on = models.DateTimeField(blank=True, null=True)  # sets the value whenever created
    #last_login = models.DateTimeField(blank=True, null=True)  # updates whenever last accessed
    slogan = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=100, blank=True)


    def __str__(self):
        return self.email