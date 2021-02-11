from rest_framework.permissions import BasePermission


class IsUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        print(obj, view, obj.user.username)
        print(obj.user != request.user)
        return obj.user != request.user
