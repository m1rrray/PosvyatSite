from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from registration.models import Registration
from registration.serializers import RegistrationSerializer


# Create your views here.

class RegistrationAPI(generics.CreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    # permission_classes = (IsAuthenticated,)


