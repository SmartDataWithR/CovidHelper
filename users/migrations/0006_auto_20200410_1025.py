# Generated by Django 2.1.5 on 2020-04-10 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200406_1820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='slogan',
        ),
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]
