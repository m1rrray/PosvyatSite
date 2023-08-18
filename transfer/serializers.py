from rest_framework import serializers

from registration.models import Registration
from .models import Transfer


class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = '__all__'

    def validate(self, data):
        phone = data.get('phone', None)

        if phone is None:
            raise serializers.ValidationError('Не указан phone.')

        try:
            registration = Registration.objects.get(phone=phone)
        except Registration.DoesNotExist:
            raise serializers.ValidationError('Такого phone нет в Registration.')

        return data