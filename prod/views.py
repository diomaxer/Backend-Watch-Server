from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from requests import Response
from rest_framework import viewsets, generics
from users.models import CustomUser
from .models import Images, Product, Sex, WatchType, Brand, Equipment, MehType, Condition, Colour,\
    Material, Glass, Waterproof, Numbers, ZipType
from .serializers import ProductSerializer, ProductSerializer2, ImagesSerializer
from rest_framework import views
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from .serializers import PropertiesSerializers
from rest_framework.permissions import IsAuthenticated


def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})


def all_view(request, *args, **kwargs):
    product = Product.objects.all()
    context = {'product': product}
    return render(request, 'all.html', context)


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductSerializer2
    permission_classes = (IsAuthenticated, )


class ImagesCreateView(generics.CreateAPIView):
    serializer_class = ImagesSerializer
    permission_classes = (IsAuthenticated, )


class UserImagesView(generics.ListAPIView):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer
    permission_classes = (IsAuthenticated, )


class ProductSpecsViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, ]
    filter_fields = ['user']

    def get_queryset(self):
        product = Product.objects.all()
        return product

    def create(self, request, *args, **kwargs):
        product_data = request.data
        new_product = Product.objects.create(
            user=CustomUser.objects.get(id=product_data["user"]),
            name=product_data["name"],
            price=product_data["price"],
            sex=Sex.objects.get(id=product_data["sex"]),
            watch_type=WatchType.objects.get(id=product_data["watch_type"]),
            brand=Brand.objects.get(id=product_data["brand"]),
            equipment=Equipment.objects.get(id=product_data["equipment"]),
            condition=Condition.objects.get(id=product_data["condition"]),
            mex_type=MehType.objects.get(id=product_data["mex_type"]),
            corpus_material=Material.objects.get(id=product_data["corpus_material"]),
            bezel_material=Material.objects.get(id=product_data["bezel_material"]),
            glass=Glass.objects.get(id=product_data["glass"]),
            waterproof=Waterproof.objects.get(id=product_data["waterproof"]),
            dial=Colour.objects.get(id=product_data["dial"]),
            numbers=Numbers.objects.get(id=product_data["numbers"]),
            bracer=Material.objects.get(id=product_data["bracer"]),
            bracer_colour=Colour.objects.get(id=product_data["bracer_colour"]),
            zip_type=ZipType.objects.get(id=product_data["zip_type"]),
            zip_material=Material.objects.get(id=product_data["zip_material"]),

        )
        new_product.save()
        serializer = ProductSerializer(new_product, many=True)
        return Response(serializer.data)


class PropertiesView(views.APIView):
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