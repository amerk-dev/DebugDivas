from rest_framework import serializers
from .models import User, SportType, Location

class SportTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportType
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['full_name', 'tg_username', 'access_token', 'refresh_token', 'sport', 'location', 'is_active', 'is_staff']