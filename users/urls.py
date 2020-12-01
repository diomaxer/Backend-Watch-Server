from django.urls import path
from rest_framework import routers

from . import views
from django.conf import settings
from django.conf.urls.static import static
from .api import CustomUserViewSet

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)