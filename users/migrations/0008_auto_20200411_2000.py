# Generated by Django 2.1.5 on 2020-04-11 18:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_customuser_slogan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='image',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='group_membership',
            field=models.CharField(choices=[('0', 'offer help'), ('1', 'find help'), ('2', 'find help anonym ')], default=2, max_length=1),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='slogan',
            field=models.TextField(blank=True, help_text='The headline of your post (will be shown on map)', max_length=1000, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9, !.?]*$', 'allowed are characters, numbers, points, question and exclamation mark')]),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='street',
            field=models.CharField(blank=True, help_text='Add your street and number or leave it out if you feel uncomfortable to share your exact location', max_length=500),
        ),
    ]
