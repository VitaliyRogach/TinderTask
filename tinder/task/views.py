from django.db.models import QuerySet
from rest_framework import generics, permissions, status, pagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import IsUser
from .serializers import *
from task import service

class ProfileListView(generics.ListAPIView):
    """Список всех профилей и их информация"""
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    # def get_queryset(self):
    #     return service.filter_group(request=self.request)
    permission_classes = [permissions.IsUser, ]

class RegistrationView(generics.CreateAPIView):
    """Регистрация"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsUser, ]

class CreateProfile(generics.CreateAPIView):
    """Создание профиля и заполнение данных"""
    queryset = Profile.objects.all()
    serializer_class = CreateProfileSerializer
    permission_classes = [permissions.IsUser, ]

class LikeView(generics.CreateAPIView):
    """Лайки пользователям"""
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsUser, ]


class UpdateLocation(generics.UpdateAPIView):
    queryset = ""
    serializer_class = UpdateLocationProfileSerializer


    def get_object(self):
        return Profile.objects.get(user=self.request.user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.geo_location = service.get_location()
        instance.save()
        return Response(status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)



class CreateLikeView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsUser, ]


    def post(self, request, *args, **kwargs):
        try:
            if Like.objects.get(user=self.request.user, profile=Profile.objects.get(pk=self.request.POST.get("profile"))):
                return Response(status=status.HTTP_202_ACCEPTED)
        except Like.DoesNotExist:
            return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        service.match(request=self.request, pk=self.request.data['profile'])
        serializer.save(user=self.request.user)