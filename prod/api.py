from .models import Images, Product, Sex, WatchType, Brand, Equipment, MehType, Condition, Colour,\
    Material, Glass, Waterproof, Numbers, ZipType
from rest_framework import viewsets, permissions
from .serializers import ProductSerializer2, ImagesSerializer, SexSerializer, WatchTypeSerializer,\
    BrandSerializer, EquipmentSerializer, MehTypeSerializer, ConditionSerializer, ColourSerializer,\
    MaterialSerializer, GlassSerializer, WaterproofSerializer, NumbersSerializer, ZipTypeSerializer


class SexViewSet(viewsets.ModelViewSet):
    queryset = Sex.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = SexSerializer


class WatchTypeViewSet(viewsets.ModelViewSet):
    queryset = WatchType.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = WatchTypeSerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = BrandSerializer


class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = EquipmentSerializer


class MehTypeViewSet(viewsets.ModelViewSet):
    queryset = MehType.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = MehTypeSerializer


class ConditionViewSet(viewsets.ModelViewSet):
    queryset = Condition.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = ConditionSerializer


class ColourViewSet(viewsets.ModelViewSet):
    queryset = Colour.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = ColourSerializer


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = MaterialSerializer


class GlassViewSet(viewsets.ModelViewSet):
    queryset = Glass.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = GlassSerializer


class WaterproofViewSet(viewsets.ModelViewSet):
    queryset = Waterproof.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = WaterproofSerializer


class NumbersViewSet(viewsets.ModelViewSet):
    queryset = Numbers.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = NumbersSerializer


class ZipTypeViewSet(viewsets.ModelViewSet):
    queryset = ZipType.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = ZipTypeSerializer


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

