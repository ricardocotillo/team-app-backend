from rest_framework import generics, viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import serializers
from . import models
from .permissions import IsMember, IsOwnerOrReadOnly


class PichangaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PichangaSerializer
    queryset = models.Pichanga.objects.all()
    permission_classes = [IsMember]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return models.Pichanga.objects.all()
        members = models.Member.objects.filter(user=self.request.user)
        return models.Pichanga.objects.filter(members__in=members)

    def perform_create(self, serializer):
        pichanga = serializer.save()
        user = self.request.user
        member = models.Member(pichanga=pichanga, user=user,
                               nickname=user.username, active=True, admin=True)
        member.save()


class PictureView(generics.CreateAPIView):
    serializer_class = serializers.PictureSerializer
    queryset = models.Picture.objects.all()


class SportViewSet(generics.ListCreateAPIView):
    serializer_class = serializers.SportSerializer
    queryset = models.Sport.objects.all()
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]