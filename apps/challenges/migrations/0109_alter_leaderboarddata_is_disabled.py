# Generated by Django 2.2.20 on 2023-11-08 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0108_alter_leaderboarddata_is_disabled_null'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaderboarddata',
            name='is_disabled',
            field=models.BooleanField(default=False),
        ),
    ]
