# Generated by Django 4.0.4 on 2022-06-07 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flc_main_app', '0025_resourcelist_fav_list_resourcelist_general_pers_dev_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resourcelist',
            old_name='title',
            new_name='name',
        ),
    ]
