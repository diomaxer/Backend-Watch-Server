from django.shortcuts import render
from requests import Response
from rest_framework import viewsets, generics, status
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
    http_method_names = ['get', 'patch', 'delete']

    def get_queryset(self):
        product = Product.objects.all()
        return product

    def partial_update(self, request, pk, *args, **kwargs):
        product = Product.objects.get(id=pk)
        if request.user.id == product.user.id:
            serializer = ProductSerializer2(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(ProductSerializer(product).data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("You don't have enough rights")

    def destroy(self, request, pk, *args, **kwargs):
        product = Product.objects.get(id=pk)
        if request.user.id == product.user.id:
            product.delete()
            return Response("Successfully deleted")
        else:
            return Response("You don't have enough rights")



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