# Generated by Django 3.1 on 2023-06-27 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='adress_line_1',
            new_name='address_line_1',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='adress_line_2',
            new_name='address_line_2',
        ),
    ]
