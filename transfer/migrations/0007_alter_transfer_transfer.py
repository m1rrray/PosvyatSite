# Generated by Django 4.2.3 on 2023-09-22 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0006_transfer_departure_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='transfer',
            field=models.CharField(choices=[('Одинцово', 'Одинцово'), ('Парка Победы', 'Парка Побед')], default=None, max_length=254),
        ),
    ]
