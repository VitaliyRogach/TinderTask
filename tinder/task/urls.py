from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *


urlpatterns = [
    path('registration/', RegistrationView.as_view()),

    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),

    path('profiles/create/', CreateProfile.as_view()),
    path('profiles/add/content/', AddContentCreateView.as_view()),
    path('profiles/list', ProfileListView.as_view()),


]