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
        tgurl = data.get('tgurl', None)
        people_custom = data.get('people_custom', [])

        if tgurl is None:
            raise serializers.ValidationError('Не указан tgurl.')

        if len(people_custom) > 4:
            raise serializers.ValidationError({'people_custom': 'Количество фамилий не должно быть больше 4'})

        try:
            registration = Registration.objects.get(tgurl=tgurl)
        except Registration.DoesNotExist:
            raise serializers.ValidationError('Такого tgurl нет в Registration.')

        return data

