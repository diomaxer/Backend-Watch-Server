from .models import CustomUser
from rest_framework import viewsets, permissions
from .serializers import CustomUserSerializer
from rest_framework.permissions import IsAuthenticated


class CustomUserViewSet(viewsets.ModelViewSet):
    "Все пользователи для watch.urls"
    queryset = CustomUser.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = CustomUserSerializer
    permission_classes = (IsAuthenticated)

