# Generated by Django 2.2.4 on 2019-08-05 17:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(old_name="user_details", new_name="UserDetails")
    ]
    atomic = False