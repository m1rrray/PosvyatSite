from rest_framework import serializers

from registration.models import Registration
from resettlement.models import Resettlement


class CustomPeopleSerializer(serializers.Serializer):
    FIO = serializers.CharField()


class ResettlementSerializer(serializers.ModelSerializer):
    people_custom = CustomPeopleSerializer(many=True)

    class Meta:
        model = Resettlement
        fields = '__all__'

    def validate(self, data):
        phone = data.get('phone', None)
        people_custom = data.get('people_custom', [])
        # save_datatransfer_to_google(data)

        if phone is None:
            raise serializers.ValidationError('Не указан phone.')

        if len(people_custom) > 4:
            raise serializers.ValidationError({'people_custom': 'Количество фамилий не должно быть больше 4'})

        try:
            registration = Registration.objects.get(phone=phone)
        except Registration.DoesNotExist:
            raise serializers.ValidationError('Такого phone нет в Registration.')

        return data
