# Generated by Django 4.2.3 on 2023-08-23 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0008_rename_otchestvo_registration_patronymic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='health',
            field=models.CharField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='registration',
            name='transfer',
            field=models.CharField(choices=[('Да, от Одинцово и обратно', 'Да, от Одинцово и обратно'), ('Да, от Парка Победы и обратно', 'Да, от Парка Победы и обратно'), ('Не нужен', 'Не нужен')], max_length=254),
        ),
    ]
