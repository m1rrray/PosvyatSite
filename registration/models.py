from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Registration(models.Model):
    GENDER_CHOICES = (
        ('Мужской', 'Мужской'),
        ('Женский', 'Женский'),
    )
    TRANSFER_CHOICES = (
        ('Да, от Одинцово и обратно', 'Да, от Одинцово и обратно'),
        ('Да, от Парка Победы и обратно', 'Да, от Парка Победы и обратно'),
        ('Не нужен', 'Не нужен')
    )
    surname = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    patronymic = models.CharField(max_length=254, blank=True)
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
    transfer = models.CharField(max_length=254, choices=TRANSFER_CHOICES)
    health = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return self.surname, self.name, self.patronymic
