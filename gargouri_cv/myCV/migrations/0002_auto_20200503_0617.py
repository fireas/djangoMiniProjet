# Generated by Django 3.0.5 on 2020-05-03 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myCV', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phoneinfo',
            old_name='skillInfo',
            new_name='phoneInfo',
        ),
    ]
