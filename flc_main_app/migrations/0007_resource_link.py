# Generated by Django 4.0.4 on 2022-06-06 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flc_main_app', '0006_resource_verified_download'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='link',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
