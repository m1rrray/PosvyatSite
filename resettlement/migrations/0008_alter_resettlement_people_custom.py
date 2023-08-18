# Generated by Django 4.2.3 on 2023-08-01 11:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resettlement', '0007_alter_resettlement_people_custom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resettlement',
            name='people_custom',
            field=models.JSONField(default=list, validators=[django.core.validators.MaxLengthValidator(4)]),
        ),
    ]
