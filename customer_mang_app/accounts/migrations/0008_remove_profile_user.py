# Generated by Django 3.0.7 on 2020-08-04 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
    ]