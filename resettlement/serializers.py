from rest_framework import serializers

from .models import Resettlement


class CustomPeopleSerializer(serializers.Serializer):
    FIO = serializers.CharField()


class ResettlementSerializer(serializers.ModelSerializer):
    people_custom = CustomPeopleSerializer(many=True)

    class Meta:
        model = Resettlement
        fields = '__all__'
