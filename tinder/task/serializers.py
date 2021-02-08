from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Content, Profile


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password',]


class ProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = User
        fields = ['name', 'pictures', 'age',]


class CreateProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
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


# class AddCommentSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = User
#         fields = '__all__'