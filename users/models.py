from django.contrib.auth.models import AbstractUser
from django.db import models
from django_google_maps import fields as map_fields
from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
    GROUPS = (
        ('0', 'offer help'),
        ('1', 'find help'),
        ('2', 'find help anonym ')
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

    # allowed
    allowed_chars = RegexValidator(r'^[a-zA-Z0-9 !.?]*$', 'allowed are characters, numbers, points, question and exclamation mark')

    group_membership = models.CharField(max_length=1, choices=GROUPS, default=2, help_text='')
    map_show_location = models.CharField(max_length=1, choices=MAP_VIEW, default=0, help_text='if you choose exact - your location will be shown exactly; if you do not want to expose your exact location choose rough')
    help_type = models.CharField(max_length=255, blank=True)
    street = models.CharField(max_length=500, blank=True, help_text='Add your street and number or leave it out if you feel uncomfortable to share your exact location')
    city_name = models.CharField(max_length=100, blank=True)
    zip_code = models.IntegerField(blank=True, default=0)
    longitude = models.FloatField(default=42, blank=True, null=True)
    latitude = models.FloatField(default=52, blank=True, null=True)
    #tel_private = models.CharField(max_length=100, blank=True)
    #tel_mobile = models.CharField(max_length=100, blank=True)
    #web = models.CharField(max_length=100, blank=True)
    #skype = models.CharField(max_length=100, blank=True)
    #linkedin = models.CharField(max_length=100, blank=True)
    user_Main_Img = models.ImageField(upload_to='images/')
    userImg_Url = models.CharField(max_length=500, blank=True, default=0)
    #profile_image = models.ImageField(upload_to='profile_image', blank=True)
    #registered_on = models.DateTimeField(blank=True, null=True)  # sets the value whenever created
    #last_login = models.DateTimeField(blank=True, null=True)  # updates whenever last accessed
    slogan = models.TextField(max_length=1000, blank=True, help_text = 'The headline of your post (will be shown on map)', validators=[allowed_chars], null=True)
    description = models.CharField(max_length=255, blank=True, help_text='The detailed description of your post (will be shown on map)', validators=[allowed_chars], null=True)


    def __str__(self):
        return self.email
