from rest_framework import serializers

from registration.models import Registration
from .models import Transfer


class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = '__all__'

    def validate(self, data):
        phone = data.get('phone', None)
        # print(data)
        massive = [data.get('surname'), data.get('name'),
                   data.get('patronymic'), data.get('email'), data.get('vkurl'),
                   data.get('tgurl'), phone]

        # save_datatransfer_to_google(massive)
        if phone is None:
            raise serializers.ValidationError('Не указан phone.')

        try:
            registration = Registration.objects.get(phone=phone)
        except Registration.DoesNotExist:
            raise serializers.ValidationError('Такого phone нет в Registration.')

        return data