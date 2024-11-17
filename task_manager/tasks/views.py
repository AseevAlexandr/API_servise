from rest_framework.exceptions import PermissionDenied

from .models import Tasks, User
from .serializers import TasksSerializers, UserSerializer
from rest_framework import viewsets, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, SAFE_METHODS


def is_admin_or_owner(request, obj):
    return request.user.is_staff or obj == request.user


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [
        permissions.IsAuthenticated,
        permissions.DjangoModelPermissionsOrAnonReadOnly
    ]

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminUser()]
        else:
            return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(password= self.request.data.get('password'))

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if not is_admin_or_owner(self.request, instance):
            raise PermissionDenied("You do not have permission to delete this object.")
        self.perform_destroy(instance)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializers
