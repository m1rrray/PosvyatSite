from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from states.models import States
from states.serializers import StateSerializer


class StatesAPI(generics.ListAPIView):
    queryset = States.objects.all()
    serializer_class = StateSerializer
<<<<<<< HEAD
    # permission_classes = (IsAuthenticated,)
=======
    # permission_classes = (IsAuthenticated,)
>>>>>>> ee60207926841042dd5b23228e2395a3135a0c6e
