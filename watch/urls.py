from django.contrib import admin
from django.urls import path, include
from prod.views import home_view
from django.conf import settings
from django.conf.urls.static import static
from prod.views import ProductCreateView, ImagesCreateView, PropertiesView
from rest_framework import routers

from users.api import CustomUserViewSet

router = routers.DefaultRouter()

# User
router.register('api/info/', CustomUserViewSet),


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),

    # PRODUCT
    path('watch/', include('prod.urls')),

    # USER
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),

    # DRF
    path('product/create/', ProductCreateView.as_view()),
    path('product/images/create/', ImagesCreateView.as_view()),
    path('product/properties/', PropertiesView.as_view(), name="properties"),

    # DJOSER
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth_token/', include('djoser.urls.authtoken')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)