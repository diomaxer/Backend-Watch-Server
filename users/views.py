from rest_framework import viewsets, generics, views
from .models import CustomUser
from .serializers import RegistrationSerializer, EmailVerificationSerializer, RequestPasswordResetEmailSerializer, SetNewPasswordSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.shortcuts import redirect


class RegistrationView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = CustomUser.objects.get(email=user_data['email'])
        user.is_active = False
        user.save()
        token = RefreshToken.for_user(user).access_token
        current_site = get_current_site(request).domain
        relative_link = reverse('email-verify')
        absolut_url = 'http://' + current_site + relative_link + "?token=" + str(token)
        email_body = 'Hi ' + user.username + \
                     ' Use link below to verify your email \n' + absolut_url
        data = {'email_body': email_body, 'to_email': user.email,
                'email_subject': 'Verify your email'}

        Util.send_email(data)
        return Response(user_data, status=status.HTTP_201_CREATED)


class VerifyEmail(views.APIView):
    serializer_class = EmailVerificationSerializer

    token_param_config = openapi.Parameter(
        'token', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            user = CustomUser.objects.get(id=payload['user_id'])
            if not user.is_active:
                user.is_active = True
                user.save()
            return redirect('https://watches360.ru/EmailVerification/confirmed')
            # return Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return redirect('https://watches360.ru/EmailVerification/expired', {'answer': 'invalid token'})
            # return Response({'error': 'Activation Expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return redirect('https://watches360.ru/EmailVerification/expired', {'answer': 'invalid token'})
            # return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)


class RequestPasswordResetEmail(generics.GenericAPIView):
    serializer_class = RequestPasswordResetEmailSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        email = request.data.get('email', '')

        if CustomUser.objects.filter(email=email).exists():
            user = CustomUser.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(
                request=request).domain
            relativeLink = reverse('password-reset-confirm', kwargs={'uidb64': uidb64, 'token': token})

            # absurl = 'http://'+current_site + relativeLink
            absurl = 'https://' + current_site + '/NewPassword/' + str(uidb64) + '/' + str(token) + '/'

            email_body = 'Hello, \n Use link below to reset your password  \n' + absurl
            data = {'email_body': email_body, 'to_email': user.email,
                    'email_subject': 'Reset your passsword'}
            Util.send_email(data)
        return Response({'success': 'We have sent you a link to reset your password'}, status=status.HTTP_200_OK)


class PasswordTokenCheckAPI(generics.GenericAPIView):
    def get(self, request, uidb64, token):
        id = smart_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(id=id)
        if not PasswordResetTokenGenerator().check_token(user, token):
            return Response({'error': 'Token is not in user anymore'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'success': True, 'massage': 'Credentials Valid', 'uidb64': uidb64, 'token': token}, status=status.HTTP_200_OK)


class SetNewPasswordAPIView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'message': 'Password reset success'}, status=status.HTTP_200_OK)


'''
class RegistrUserView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)
            
class SignUp(generic.CreateView):
   form_class = CustomUserCreationForm
   success_url = reverse_lazy('login')
   template_name = 'registration/signup.html'


def signup_view(request):
    form = UserForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, 'registration/signup.html', context)

'''
