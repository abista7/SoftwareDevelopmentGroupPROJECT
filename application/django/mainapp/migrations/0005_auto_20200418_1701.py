# Generated by Django 3.0.5 on 2020-04-19 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20200418_1656'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friend',
            old_name='match_time',
            new_name='friend_time',
        ),
        migrations.RenameField(
            model_name='friend',
            old_name='is_matched',
            new_name='is_friend',
        ),
    ]
