from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from PosvyatSite.validators import validate_vk_url, validate_tg_link


class Transfer(models.Model):
    surname = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    patronymic = models.CharField(max_length=254, blank=True)
    email = models.EmailField(max_length=254)
    vkurl = models.CharField(unique=True, validators=[validate_vk_url], max_length=255)
    tgurl = models.CharField(unique=True, validators=[validate_tg_link],  max_length=254)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
