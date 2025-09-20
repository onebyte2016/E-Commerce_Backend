from rest_framework.serializers import ModelSerializer, Serializer
from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'username')

class RegisterUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("email","username", "password")
        extra_kwargs = {"password":{"write_only":True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user


class LoginUserSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")
        user = authenticate(email=email, password=password)  # uses EmailBackend now

        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect email or password.")
