from rest_framework import routers
from .views import ProductSpecsViewSet
from .api import ImagesViewSet

router = routers.DefaultRouter()

# Product
router.register('api/product_get', ProductSpecsViewSet, 'product_get')

# Images
router.register('api/images', ImagesViewSet, 'images')


urlpatterns = router.urls
