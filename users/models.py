from django.contrib.auth.models import AbstractUser
from django.db import models
from django_google_maps import fields as map_fields
from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
    GROUPS = (
        ('0', 'offer help'),
        ('1', 'find help'),
        ('2', 'find help anonymously'),
        ('3', 'present a shop')
    )

    SHOP_GROUPS = (
        ('Grocery', 'Grocery Store'),
        ('Pharmacy', 'Pharmacy'),
        ('Other', 'Other Store')
    )

    MAP_VIEW = (
        ('0', 'rough'),
        ('1', 'exact')
    )

    # allowed
    allowed_chars = RegexValidator(r'^[a-zA-Z0-9 !.?]*$', 'allowed are characters, numbers, points, question and exclamation mark')

    group_membership = models.CharField(max_length=1, choices=GROUPS, default=2, help_text='')
    map_show_location = models.CharField(max_length=1, choices=MAP_VIEW, default=0, help_text='if you choose exact - your location will be shown exactly; if you do not want to expose your exact location choose rough')
    help_type = models.CharField(max_length=255, blank=True, null=True)
    
    street = models.CharField(max_length=500, blank=True, help_text='Add your street and number or leave it out if you feel uncomfortable to share your exact location')
    city_name = models.CharField(max_length=100, blank=True)
    zip_code = models.IntegerField(blank=True, default=0)
    longitude = models.FloatField(default=42, blank=True, null=True)
    latitude = models.FloatField(default=52, blank=True, null=True)
    user_Main_Img = models.ImageField(upload_to='images/', blank=True, default=0)
    userImg_Url = models.CharField(max_length=500, blank=True, default=0)
    #last_login = models.DateTimeField(blank=True, null=True)  # updates whenever last accessed
    slogan = models.TextField(max_length=1000, blank=True, help_text = 'The headline of your post (will be shown on map)', validators=[allowed_chars], null=True)
    description = models.CharField(max_length=255, blank=True, help_text='The detailed description of your post (will be shown on map)', validators=[allowed_chars], null=True)

    # specific properties for shops
    shop_type = models.CharField(max_length=255, choices=SHOP_GROUPS, blank=True)
    shop_title = models.CharField(max_length=100, blank=True)
    shop_open = models.BooleanField(default=False, null=True)
    shop_closed = models.BooleanField(default=False, null=True)
    shop_deliver = models.BooleanField(default=False, null=True)
    shop_pickup = models.BooleanField(default=False, null=True)


    def __str__(self):
        return self.email
