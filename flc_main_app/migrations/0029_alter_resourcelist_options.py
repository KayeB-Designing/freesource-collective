# Generated by Django 4.0.4 on 2022-06-07 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flc_main_app', '0028_resourcelist_creator'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resourcelist',
            options={'ordering': ['name']},
        ),
    ]
