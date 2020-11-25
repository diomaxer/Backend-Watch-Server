from .models import Product, Images
from rest_framework import viewsets, permissions
from .serializers import ProductSerializer2, ImagesSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProductSerializer2


class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = ImagesSerializer
