# Generated by Django 4.2.16 on 2024-10-22 01:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0002_user_bia'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='bia',
            new_name='bio',
        ),
    ]