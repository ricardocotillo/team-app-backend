from rest_framework import permissions
from .models import Member


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

class IsMember(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        members = Member.objects.filter(user=request.user)
        for member in members:
            if member.org == obj:
                return True
        return False
        