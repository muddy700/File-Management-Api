from rest_framework import generics, permissions, viewsets
from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny,
        # permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer

   