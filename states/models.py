from django.db import models


class States(models.Model):
    registration = models.BooleanField(default=False)
    transfer = models.BooleanField(default=False)
    resettlement = models.BooleanField(default=False)
