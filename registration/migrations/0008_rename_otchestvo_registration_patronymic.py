# Generated by Django 4.2.3 on 2023-08-18 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0007_alter_registration_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='otchestvo',
            new_name='patronymic',
        ),
    ]