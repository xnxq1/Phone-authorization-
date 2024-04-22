# Generated by Django 4.2.11 on 2024-04-22 03:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_referralprogram_referral_users_delete_referral'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referralprogram',
            name='referral_users',
            field=models.ManyToManyField(blank=True, related_name='referral', to=settings.AUTH_USER_MODEL),
        ),
    ]
