# Generated by Django 3.0.8 on 2020-07-22 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likes',
            name='users',
        ),
    ]
