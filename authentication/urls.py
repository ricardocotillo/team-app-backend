from unicodedata import name
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import MyObtainTokenPairView, RegisterView

urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='obtain_token_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('register/', RegisterView.as_view(), name='register'),
]