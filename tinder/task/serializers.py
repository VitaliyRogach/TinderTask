from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения юзера"""
    class Meta:
        model = User
        fields = ['username', 'password']


class ProfileSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения профилей юзеров"""
    user = UserSerializer()

    class Meta:
        model = UserInf
        fields = ['user', 'image', 'name', 'surname', ]


class CreateProfileSerializer(serializers.ModelSerializer):
    """Сериализатор для создания профиля юзера"""
    class Meta:
        model = UserInf
        fields = '__all__'


class AddContentSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = Content
        fields = '__all__'


class CreateAddContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Content
        fields = '__all__'