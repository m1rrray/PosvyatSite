from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Registration(models.Model):
    surname = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    otchestvo = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    vkurl = models.URLField(unique=True)
    tgurl = models.CharField(unique=True, max_length=254)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    birth_date = models.DateField(max_length=254)
    sex = models.CharField(max_length=50)
    univer = models.CharField(max_length=254)
    faculty = models.CharField(max_length=254)
    program = models.CharField(max_length=254)
    year = models.IntegerField()
    group = models.CharField(max_length=254)
    transfer = models.CharField(max_length=254)
    health = models.CharField(max_length=254)

    def __str__(self):
        return self.surname, self.name, self.otchestvo
