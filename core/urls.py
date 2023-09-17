from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import UserRegistrationView

urlpatterns = [
    path("register/", view=UserRegistrationView.as_view(), name='register'),
    path("jwt/create/", view=TokenObtainPairView.as_view(), name='jwt-create'),
    path("jwt/refresh/", view=TokenRefreshView.as_view(), name='jwt-refresh'),
]
