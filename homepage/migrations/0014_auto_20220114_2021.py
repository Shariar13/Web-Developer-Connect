# Generated by Django 3.1.8 on 2022-01-14 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0013_friend_list_request_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friend_list',
            old_name='request_count',
            new_name='friend_count',
        ),
    ]
