from django.db import models

from PosvyatSite.validators import validate_vk_url, validate_tg_link
from phonenumber_field.modelfields import PhoneNumberField


class Resettlement(models.Model):
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100, blank=True)
    vkurl = models.CharField(unique=True, validators=[validate_vk_url], max_length=255)
    tgurl = models.CharField(unique=True, validators=[validate_tg_link], max_length=254)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    program = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    year = models.IntegerField()
    people_custom = models.JSONField(default=list, blank=True)

