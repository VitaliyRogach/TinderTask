from django.urls import path, include
from .views import *


urlpatterns = [
    path('user/<int:pk>/', UserPage.as_view()),

]