from django.db import models


# def validate_people_custom(value):
#     if not isinstance(value, list):
#         raise ValidationError('Значение должно быть списком')
#     print(value)
#     if len(value) > 4:
#         raise ValidationError('Количество фамилий не должно быть больше 4')
# 
#     for person in value:
#         if not isinstance(person, dict):
#             raise ValidationError('Каждый элемент списка должен быть словарем')
# 
#         if 'FIO' not in person:
#             raise ValidationError('У каждого словаря должно быть поле "FIO"')


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
