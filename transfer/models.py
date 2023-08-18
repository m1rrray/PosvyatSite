from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Transfer(models.Model):
    surname = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    patronymic = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    vkurl = models.URLField(unique=True)
    tgurl = models.CharField(unique=True, max_length=254)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
