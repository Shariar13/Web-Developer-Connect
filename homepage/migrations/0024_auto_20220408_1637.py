# Generated by Django 3.1.2 on 2022-04-08 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0023_auto_20220126_1218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='eyes',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='hair',
            new_name='framework',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='height',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='weight',
            new_name='skills',
        ),
    ]
