from django.db.models import QuerySet
from rest_framework import generics, permissions, status, pagination
from rest_framework.response import Response
from rest_framework.views import APIView


from .serializers import *
from task import service

class ProfileListView(generics.ListAPIView):
    """Список всех профилей и их информация"""
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    def get_queryset(self):
        return service.filter_group(request=self.request)

class RegistrationView(generics.CreateAPIView):
    """Регистрация"""
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CreateProfile(generics.CreateAPIView):
    """Создание профиля и заполнение данных"""
    queryset = Profile.objects.all()
    serializer_class = CreateProfileSerializer


class LikeView(generics.CreateAPIView):
    """Лайки пользователям"""
    queryset = Like.objects.all()
    serializer_class = LikeSerializer



