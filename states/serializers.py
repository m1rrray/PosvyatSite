from rest_framework import serializers

from states.models import States


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = States
        fields = '__all__'
