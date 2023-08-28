import re

from django.core.validators import RegexValidator
from rest_framework.exceptions import ValidationError


def validate_vk_url(value):
    regex = r'^(www\.)?vk\.com/.*$'
    if not re.match(regex, value):
        raise ValidationError('URL должен быть в формате vk.com/<something>')


def validate_tg_link(value):
    regex = r'^@[\w_]+$'
    if not re.match(regex, value):
        raise ValidationError('URL должен быть в формате @<something>')
