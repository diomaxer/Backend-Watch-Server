from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Images
from rest_framework import viewsets, status
from .serializers import ImagesSerializer
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend


class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer
    parser_classes = (JSONParser, FormParser, MultiPartParser)
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    filter_backends = [DjangoFilterBackend, ]
    filter_fields = ['ad']

    @action(detail=True, methods=['POST'])
    def uploadImage(self, request, pk=None):
        ad = self.get_object()
        image = ad.image
        serializer = ImagesSerializer(image, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)

    def partial_update(self, request, pk, *args, **kwargs):
        image = Images.objects.get(id=pk)
        if request.user.id == image.ad.user.id:
            serializer = ImagesSerializer(image, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("You don't have enough rights")

    def destroy(self, request, pk, *args, **kwargs):
        image = Images.objects.get(id=pk)
        if request.user.id == image.ad.user.id:
            image.delete()
            return Response("Successfully deleted")
        else:
            return Response("You don't have enough rights")

