# Generated by Django 4.0.4 on 2022-06-06 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flc_main_app', '0005_resource_general_pers_dev_resource_goal_setting_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='verified_download',
            field=models.BooleanField(default=False),
        ),
    ]
