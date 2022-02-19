from rest_framework import generics, viewsets
from rest_framework import permissions
from . import serializers
from . import models
from .permissions import IsMember


class OrganizationViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.OrganizationSerializer
    queryset = models.Organization.objects.all()
    permission_classes = [IsMember]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return models.Organization.objects.all()
        members = models.Member.objects.filter(user=self.request.user)
        return models.Organization.objects.filter(members__in=members)

    def perform_create(self, serializer):
        org = serializer.save()
        user = self.request.user
        member = models.Member(org=org, user=user, nickname=user.username, active=True, admin=True)
        member.save()


class PictureView(generics.CreateAPIView):
    serializer_class = serializers.PictureSerializer
    queryset = models.Picture.objects.all()


class SportViewSet(generics.ListCreateAPIView):
    serializer_class = serializers.SportSerializer
    queryset = models.Sport.objects.all()
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]