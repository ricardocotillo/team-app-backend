from rest_framework import permissions

from .models import Member

class IsMember(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        members = Member.objects.filter(user=request.user)
        for member in members:
            if member.org == obj:
                return True
        return False
        