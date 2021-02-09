from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Content, Profile, Like


class UserSerializer(serializers.ModelSerializer):
    """Для регистрации пользователей"""
    class Meta:
        model = User
        fields = ['username', 'password',]


class ProfileSerializer(serializers.ModelSerializer):
    """Для представления информации профиля"""
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ['user', 'name', 'pictures', 'age', 'description', 'group']


class CreateProfileSerializer(serializers.ModelSerializer):
    """Для создания профиля и заполнения информации"""
    class Meta:
        model = Profile
        fields = ['user','name', 'description', 'age', 'pictures', 'group',]

class LikeSerializer(serializers.ModelSerializer):
    """Для создания лайков"""
    class Meta:
        model = Like
        fields = ['like', 'userliker', 'profile']


# class AddContentSerializer(serializers.ModelSerializer):
#     profile = ProfileSerializer()
#
#     class Meta:
#         model = Content
#         fields = '__all__'
#
#
# class CreateAddContentSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Content
#         fields = ['profile', 'image', 'description',]


