from django.contrib import admin
from django.urls import path, include
from prod.views import all_view, home_view, post
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from users.views import lk_view
from prod import views
from prod.views import ProductCreateView, ImagesCreateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('all/', all_view, name='all'),
    path('', home_view, name='home'),

    # PRODUCT

    path('create/', post, name='create'),
    path('watch/', include('prod.urls')),
    path('<int:pk>', views.ProductDetailView.as_view(), name='product_detail_view'),

    # USER
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('lk/', lk_view, name='lk'),

    # DRF
    path('product/create/', ProductCreateView.as_view()),
    path('product/images/create/', ImagesCreateView.as_view()),

    # DJOSER
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth_token/', include('djoser.urls.authtoken')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)