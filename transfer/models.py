from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from PosvyatSite.validators import validate_vk_url, validate_tg_link


class Transfer(models.Model):
    TRANSFER_CHOICES = (
        ('Да, от Одинцово и обратно', 'Да, от Одинцово и обратно'),
        ('Да, от Парка Победы и обратно', 'Да, от Парка Победы и обратно'),
    )
    TIMES = (
        ('15:15', '15:15'),
        ('15:35', '15:35'),
        ('15:55', '15:55'),
        ('17:35', '17:35'),
        ('16:45', '16:45'),
        ('17:25', '17:25'),
        ('17:45', '17:45'),
        ('18:25', '18:25'),
        ('18:45', '18:45'),
        ('19:25', '19:25'),
    )
    surname = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    patronymic = models.CharField(max_length=254, blank=True)
    email = models.EmailField(max_length=254)
    vkurl = models.CharField(unique=True, validators=[validate_vk_url], max_length=255)
    tgurl = models.CharField(unique=True, validators=[validate_tg_link],  max_length=254)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    transfer = models.CharField(max_length=254, choices=TRANSFER_CHOICES, default=None)
    departure_time = models.CharField(max_length=30, choices=TIMES, default=None)
