# Generated by Django 4.0.4 on 2022-06-07 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flc_main_app', '0015_comment_author_comment_resource'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='resource',
            field=models.ForeignKey(default=16, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='flc_main_app.resource'),
        ),
    ]