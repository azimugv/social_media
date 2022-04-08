# Generated by Django 4.0.3 on 2022-03-16 18:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0006_post_dislike_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hahas',
            field=models.ManyToManyField(blank=True, related_name='haha', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='loves',
            field=models.ManyToManyField(blank=True, related_name='loves', to=settings.AUTH_USER_MODEL),
        ),
    ]
