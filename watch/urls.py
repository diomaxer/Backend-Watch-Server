from django.contrib import admin
from django.urls import path, include
from prod.views import home_view, MyProductViewList
from django.conf import settings
from django.conf.urls.static import static
from prod.views import ProductCreateView, ImagesCreateView, PropertiesView, UserImagesView
from rest_framework import routers
from users.api import CustomUserViewSet
from users.views import RegistrationView

router = routers.DefaultRouter()

# User
router.register('api/info/', CustomUserViewSet),


urlpatterns = [
    path('be/app/admin/', admin.site.urls),
    path('be/app/', home_view, name='home'),

    # PRODUCT
    path('be/app/watch/', include('prod.urls')),

    # USER
    # path('users/', include('users.urls')),
    # path('users/', include('django.contrib.auth.urls')),

    # DRF
    path('be/app/product/create/', ProductCreateView.as_view()),
    path('be/app/product/images/create/', ImagesCreateView.as_view()),
    path('be/app/product/images/users/', UserImagesView.as_view()),
    path('be/app/product/my_list', MyProductViewList.as_view()),
    path('be/app/product/properties/', PropertiesView.as_view(), name="properties"),
    path('be/app/registr/', RegistrationView.as_view(), name='registr'),

    # DJOSER
    path('be/app/api/v1/auth/', include('djoser.urls')),
    path('be/app/api/v1/auth_token/', include('djoser.urls.authtoken')),

    # Authentication
    path('be/app/authentication/', include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)