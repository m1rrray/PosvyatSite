# Generated by Django 4.2.3 on 2023-07-30 01:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resettlement', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='name',
            new_name='FIO',
        ),
        migrations.RemoveField(
            model_name='person',
            name='otchestvo',
        ),
        migrations.RemoveField(
            model_name='person',
            name='surname',
        ),
    ]
