from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import User, SportType, Location
from .serializers import UserSerializer, SportTypeSerializer, LocationSerializer

class SportTypeViewSet(viewsets.ModelViewSet):
    queryset = SportType.objects.all()
    serializer_class = SportTypeSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer