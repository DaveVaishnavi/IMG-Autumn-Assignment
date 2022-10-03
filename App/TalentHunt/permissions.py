from rest_framework.permissions import BasePermission


class IsAllowedToAccessScore(BasePermission):
    message = "Permission Denied"

    def has_object_permission(self, request, view, obj):
        if request.year == 2:
            return False

        return True


class IsAllowedToAssignQuestion(BasePermission):
    message = "Permission Denied"
