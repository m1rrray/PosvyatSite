from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Transfer(models.Model):
    surname = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    patronymic = models.CharField(max_length=254, blank=True)
    email = models.EmailField(max_length=254)
    vkurl = models.URLField(unique=True)
    tgurl = models.CharField(unique=True, max_length=254)
    phone = PhoneNumberField(null=False, blank=False, unique=True)

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}, {str(self.phone)}, {self.email}, {self.vkurl}, {self.tgurl}"