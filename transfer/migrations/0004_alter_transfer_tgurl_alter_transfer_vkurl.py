# Generated by Django 4.2.3 on 2023-08-28 01:12

import PosvyatSite.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0003_alter_transfer_patronymic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='tgurl',
            field=models.CharField(max_length=254, unique=True, validators=[PosvyatSite.validators.validate_tg_link]),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='vkurl',
            field=models.CharField(max_length=255, unique=True, validators=[PosvyatSite.validators.validate_vk_url]),
        ),
    ]
