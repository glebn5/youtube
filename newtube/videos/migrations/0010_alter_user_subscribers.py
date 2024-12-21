# Generated by Django 5.1.1 on 2024-12-04 17:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0009_remove_user_subscribers_user_subscribers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='subscribers',
            field=models.ManyToManyField(blank=True, related_name='subscriptions', to=settings.AUTH_USER_MODEL),
        ),
    ]