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
        fields = (
            CustomUser.tg_username.field.name,
            CustomUser.sport_type.field.name,
            CustomUser.is_active.field.name,
            CustomUser.is_staff.field.name
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            CustomUser.tg_username.field.name,
            CustomUser.email.field.name
        )


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = (
            CustomUser.tg_username.field.name,
            CustomUser.email.field.name,
            CustomUser.password.field.name
        )

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            tg_username=validated_data['tg_username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user