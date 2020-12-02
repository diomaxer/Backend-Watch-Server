from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.response import Response

from .models import Images
from rest_framework import viewsets
from .serializers import ImagesSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action


class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    permissions_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, )
    serializer_class = ImagesSerializer
    parser_classes = (JSONParser, FormParser, MultiPartParser)

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
