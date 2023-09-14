from rest_framework import serializers

from registration.models import Registration
from .models import Transfer


class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = '__all__'

    def validate(self, data):
        phone = data.get('phone', None)
        transfer = data.get('transfer')
        departure_time = data.get('departure_time')

        # massive = [data.get('surname'), data.get('name'),
        #            data.get('patronymic'), data.get('email'), data.get('vkurl'),
        #            data.get('tgurl'), phone, transfer, departure_time]

        if phone is None:
            raise serializers.ValidationError('Не указан phone.')

        count_transfer = Transfer.objects.filter(transfer=transfer, departure_time=departure_time)
        if len(count_transfer) >= 46:
            raise serializers.ValidationError('this is the route places have ended')

        try:
            registration = Registration.objects.get(phone=phone)
        except Registration.DoesNotExist:
            raise serializers.ValidationError('Такого phone нет в Registration.')

        return data
