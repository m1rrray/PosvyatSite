from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from states.models import States
from states.serializers import StateSerializer


class StatesAPI(generics.ListAPIView):
    queryset = States.objects.all()
    serializer_class = StateSerializer
    # permission_classes = (IsAuthenticated,)
