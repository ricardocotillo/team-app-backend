from rest_framework import viewsets

from .serializers import OrganizationSerializer
from .models import Organization, Member
from .permissions import IsMember

# Create your views here.
class OrganizationViewSet(viewsets.ModelViewSet):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
    permission_classes = [IsMember]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Organization.objects.all()
        members = Member.objects.filter(user=self.request.user)
        return Organization.objects.filter(members__in=members)

    def perform_create(self, serializer):
        org = serializer.save()
        user = self.request.user
        member = Member(org=org, user=user, nickname=user.username, active=True, admin=True)
        member.save()