# Generated by Django 4.2.3 on 2023-08-28 01:34

import PosvyatSite.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0010_alter_registration_patronymic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='tgurl',
            field=models.CharField(max_length=254, unique=True, validators=[PosvyatSite.validators.validate_tg_link]),
        ),
        migrations.AlterField(
            model_name='registration',
            name='vkurl',
            field=models.CharField(max_length=255, unique=True, validators=[PosvyatSite.validators.validate_vk_url]),
        ),
    ]
