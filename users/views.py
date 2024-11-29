from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from users.models import User
from users.permissions import IsAdmin, IsSelf
from users.serializers import UserSerializer


class UserAdViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = (AllowAny,)
        elif self.action == 'list':
            self.permission_classes = (IsAdmin,)
        elif self.action in ['retrieve', 'update']:
            self.permission_classes = (IsAuthenticated, IsSelf | IsAdmin)
        elif self.action == 'destroy':
            self.permission_classes = (IsAuthenticated, IsSelf | IsAdmin)
        return super().get_permissions()

    # def get_queryset(self):
    #     return User.objects.filter(id=self.request.user.id)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(self.request.data.get('password'))
        user.save()

    def perform_update(self, serializer):
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
