from rest_framework import generics
from rest_framework import permissions
from . import serializers
from . import models

class PictureView(generics.CreateAPIView):
    serializer_class = serializers.PictureSerializer
    queryset = models.Picture.objects.all()


class SportViewSet(generics.ListCreateAPIView):
    serializer_class = serializers.SportSerializer
    queryset = models.Sport.objects.all()
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]