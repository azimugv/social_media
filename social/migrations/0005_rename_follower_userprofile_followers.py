# Generated by Django 4.0.3 on 2022-03-16 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_userprofile_follower'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='follower',
            new_name='followers',
        ),
    ]
