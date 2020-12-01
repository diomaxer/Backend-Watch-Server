from .models import Images
from rest_framework import viewsets, permissions
from .serializers import ImagesSerializer


class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = ImagesSerializer

