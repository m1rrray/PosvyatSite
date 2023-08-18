from rest_framework import serializers

from registration.models import Registration
from .models import Transfer


class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = '__all__'

    def validate(self, data):
        tgurl = data.get('tgurl', None)

        if tgurl is None:
            raise serializers.ValidationError('Не указан tgurl.')

        try:
            registration = Registration.objects.get(tgurl=tgurl)
        except Registration.DoesNotExist:
            raise serializers.ValidationError('Такого tgurl нет в Registration.')

        return data