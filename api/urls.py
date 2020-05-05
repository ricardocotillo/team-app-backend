from . import views
from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView, TokenObtainPairView


router = routers.SimpleRouter()
router.register('pichangas', views.PichangaViewSet, basename='pichangas')
router.register('users', views.UserViewSet, basename='users')
router.register('profiles', views.ProfileViewSet, basename='profiles')

urlpatterns = [
    path('pictures/', views.PictureView.as_view(), name='pictures'),
    path('sports/', views.SportViewSet.as_view(), name='sports'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='verify'),
]
urlpatterns = urlpatterns + router.urls
