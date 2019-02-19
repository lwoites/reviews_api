from rest_framework import permissions


class IsReviewer(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to view and edit it.
    """

    def has_object_permission(self, request, view, obj):
        return obj.reviewer == request.user
