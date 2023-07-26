from django.shortcuts import render
from rest_framework import generics

from registration.models import Registration
from registration.serializers import RegistrationSerializer


# Create your views here.

class RegistrationAPI(generics.ListCreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    # permission_classes = (IsAuthenticated, )
    # authentication_classes = (TokenAuthentication, )