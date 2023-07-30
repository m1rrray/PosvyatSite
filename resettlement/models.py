from django.db import models


class Resettlement(models.Model):
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    otchestvo = models.CharField(max_length=100)
    vkurl = models.URLField()
    tgurl = models.CharField(max_length=100)
    program = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    year = models.IntegerField()
    people_custom = models.JSONField(default=list)
