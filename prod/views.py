from django.shortcuts import render
from requests import Response
from rest_framework import viewsets, generics
from .models import Images, Product, Sex, WatchType, Brand, Equipment, MehType, Condition, Colour,\
    Material, Glass, Waterproof, Numbers, ZipType
from .serializers import ProductSerializer, ProductSerializer2, ImagesSerializer
from rest_framework import views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.status import HTTP_200_OK
from .serializers import PropertiesSerializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})


def all_view(request, *args, **kwargs):
    product = Product.objects.all()
    context = {'product': product}
    return render(request, 'all.html', context)


class ProductCreateView(generics.CreateAPIView):
    "Создание объявления"
    serializer_class = ProductSerializer2
    permission_classes = (IsAuthenticated, )


class ImagesCreateView(generics.CreateAPIView):
    "Загрузка фотографий в объявления"
    serializer_class = ImagesSerializer
    permission_classes = (IsAuthenticated, )


class UserImagesView(generics.ListAPIView):
    "Методы Get Patch Delete для фотографий в объявлениях"
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer
    permission_classes = (IsAuthenticated, )


class ProductSpecsViewSet(viewsets.ModelViewSet):
    "Методы GET PATCH DELETE для объявлений"
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['name', 'price', 'sex']
    search_fields = ['name', 'brand__name', ]
    ordering_films = ['price', 'name']


class PropertiesView(views.APIView):
    "Передача всех данных в моделях с ForeignKey"
    def get(self, request, *args, **kwargs):
        properties = {
            'sex': Sex.objects.all(),
            'watch_type': WatchType.objects.all(),
            'brand': Brand.objects.all(),
            'equipment': Equipment.objects.all(),
            'meh_type': MehType.objects.all(),
            'condition': Condition.objects.all(),
            'colour': Colour.objects.all(),
            'material': Material.objects.all(),
            'glass': Glass.objects.all(),
            'waterproof': Waterproof.objects.all(),
            'numbers': Numbers.objects.all(),
            'zip_type': ZipType.objects.all()
        }
        serializer = PropertiesSerializers(properties)
        return Response (serializer.data, status=HTTP_200_OK)
