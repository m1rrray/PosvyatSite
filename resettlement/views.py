from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from resettlement.models import Resettlement
from resettlement.serializers import ResettlementSerializer


class ResettlementAPI(generics.ListCreateAPIView):
    queryset = Resettlement.objects.all()
    serializer_class = ResettlementSerializer
    permission_classes = (IsAuthenticated,)






