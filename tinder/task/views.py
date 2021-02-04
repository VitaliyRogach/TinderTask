from django.db.models import QuerySet
from rest_framework import generics, permissions, status, pagination
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from task import service

class ProfileListView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = ''

    def get_queryset(self):
        return service.filter_group(request=self.request)


class AddContentCreateView(generics.CreateAPIView):
    queryset = Content.objects.all()
    serializer_class = CreateAddContentSerializer