# Generated by Django 2.2.20 on 2023-04-15 08:14

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_add_jwt_access_token_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='github_url',
            field=models.URLField(blank=True, null=True, validators=[accounts.models.validate_github_url]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='google_scholar_url',
            field=models.URLField(blank=True, null=True, validators=[accounts.models.validate_google_scholar_url]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='linkedin_url',
            field=models.URLField(blank=True, null=True, validators=[accounts.models.validate_linkedin_url]),
        ),
    ]
