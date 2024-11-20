from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """ Проверяет, является ли пользователь Администратором. """
    def has_permission(self, request, view):
        return request.user.role == 'admin'


class IsAuthor(permissions.BasePermission):
    """ Проверяет, является ли пользователь автором. """
    def has_object_permission(self, request, view, obj):
        if obj.author == request.user:
            return True
        return False
