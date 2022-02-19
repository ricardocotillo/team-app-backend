from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView, TokenObtainPairView

from organization.views import OrganizationViewSet
from authentication.views import UserVieset

from . import views


router = routers.SimpleRouter()
router.register('organizations', OrganizationViewSet)
router.register('users', UserVieset)

urlpatterns = [
    path('pictures/', views.PictureView.as_view(), name='pictures'),
    path('sports/', views.SportViewSet.as_view(), name='sports'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='verify'),
]
urlpatterns = urlpatterns + router.urls
