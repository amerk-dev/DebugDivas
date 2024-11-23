from rest_framework import serializers
from .models import CustomUser, SportType, Location

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
        model = CustomUser
        fields = ['tg_username', 'sport', 'is_active', 'is_staff']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('tg_username', 'email')


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('tg_username', 'email', 'password')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            tg_username=validated_data['tg_username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user