# Generated by Django 4.0.3 on 2022-04-18 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0005_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='owner',
        ),
    ]
