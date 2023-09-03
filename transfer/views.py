from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from transfer.models import Transfer
from transfer.serializers import TransferSerializer


class TransferAPI(generics.CreateAPIView):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer
    # permission_classes = (IsAuthenticated, )
