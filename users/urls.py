from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import VerifyEmail, RequestPasswordResetEmail, PasswordTokenCheckAPI, SetNewPasswordAPIView


urlpatterns = [
    # path('register/', RegistrationView.as_view(), name='register'),
    path('email-verify/', VerifyEmail.as_view(), name='email-verify'),
    path('request-reset-email/', RequestPasswordResetEmail.as_view(), name="request-reset-email"),
    path('password-reset/<uidb64>/<token>/', PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    # path('signup/', views.SignUp.as_view(), name='signup'),
    path('password-reset-complete/', SetNewPasswordAPIView.as_view(), name='password-reset-complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
