from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .api import ProductViewSet, ImagesViewSet
from .views import ProductSpecsView

router = routers.DefaultRouter()
router.register('api/product_post', ProductViewSet, 'product_post')
router.register('api/product_get', ProductSpecsView, 'product_get')
router.register('api/images', ImagesViewSet, 'images')

urlpatterns = [
    path('<int:pk>', views.ProductDetailView.as_view(), name='product_detail_view'),
]

urlpatterns = router.urls
