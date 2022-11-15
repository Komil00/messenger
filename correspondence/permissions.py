from rest_framework import permissions


class UpdatePermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        pass
