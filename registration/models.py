from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Registration(models.Model):
    GENDER_CHOICES = (
        ('Мужской', 'Мужской'),
        ('Женский', 'Женский'),
    )
    surname = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    otchestvo = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    vkurl = models.URLField(unique=True)
    tgurl = models.CharField(unique=True, max_length=254)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    birth_date = models.DateField(max_length=254)
    sex = models.CharField(max_length=20, choices=GENDER_CHOICES)
    univer = models.CharField(max_length=254)
    faculty = models.CharField(max_length=254)
    program = models.CharField(max_length=254)
    year = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    group = models.CharField(max_length=254)
    transfer = models.CharField(max_length=254)
    health = models.CharField(max_length=254)

    def __str__(self):
        return self.surname, self.name, self.otchestvo
