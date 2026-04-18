from rest_framework.permissions import BasePermission

class IsCitizen(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'citizen'

class IsVolunteer(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'volunteer'

class IsAuthority(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'authority'