from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .api import ProductViewSet, ImagesViewSet, SexViewSet, WatchTypeViewSet, BrandViewSet, EquipmentViewSet,\
    MehTypeViewSet, ConditionViewSet, ColourViewSet, MaterialViewSet, GlassViewSet, WaterproofViewSet,\
    NumbersViewSet, ZipTypeViewSet
from .views import ProductSpecsView

router = routers.DefaultRouter()
# Product
router.register('api/product_post', ProductViewSet, 'product_post')
router.register('api/product_get', ProductSpecsView, 'product_get')

# Components
router.register('api/sex', SexViewSet, 'sex')
router.register('api/watchtype', WatchTypeViewSet, 'watchtype')
router.register('api/brand', BrandViewSet, 'brand')
router.register('api/equipment', EquipmentViewSet, 'equipment')
router.register('api/mehtype', MehTypeViewSet, 'mehtype')
router.register('api/condition', ConditionViewSet, 'condition')
router.register('api/colour', ColourViewSet, 'colour')
router.register('api/material', MaterialViewSet, 'material')
router.register('api/glass', GlassViewSet, 'glass')
router.register('api/waterproof', WaterproofViewSet, 'waterproof')
router.register('api/numbers', NumbersViewSet, 'numbers')
router.register('api/ziptype', ZipTypeViewSet, 'ziptype')

# Images
router.register('api/images', ImagesViewSet, 'images')

urlpatterns = [
    path('<int:pk>', views.ProductDetailView.as_view(), name='product_detail_view'),
]

urlpatterns = router.urls
