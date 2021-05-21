from rest_framework import serializers
from .models import CustomUser
from rest_framework.exceptions import AuthenticationFailed

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode


class CustomUserSerializer(serializers.ModelSerializer):
    "Сериализатор модели пользователя"

    class Meta:
        model = CustomUser
        fields = [
            'email',
            'username',
            'phone',
            'city',
            'company',
            'avatar',
        ]


class RegistrationSerializer(serializers.ModelSerializer):
    "Сериализатор для регистрации"

    password = serializers.CharField(max_length=68, min_length=6)

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'city', 'company', 'phone', 'avatar', ]

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class EmailVerificationSerializer(serializers.ModelSerializer):
    "Сериализатор подтверждения по EMAIL"

    token = serializers.CharField(max_length=255)

    class Meta:
        model = CustomUser
        fields = ['token', ]


class RequestPasswordResetEmailSerializer(serializers.Serializer):
    "Сериализатор для запроса на смену пароля"

    email = serializers.EmailField(min_length=2)

    class Meta:
        model = CustomUser
        fields = ['email']


class SetNewPasswordSerializer(serializers.Serializer):
    "Сериализатор для смены пароля"

    password = serializers.CharField(min_length=6, max_length=68, write_only=True)
    token = serializers.CharField(min_length=1, write_only=True)
    uidb64 = serializers.CharField(min_length=1, write_only=True)

    class Meta:
        fields = ['password', 'token', 'uidb64']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')

            id = force_str(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('The reset link is invalid', 401)

            user.set_password(password)
            user.save()

            return user
        except Exception as e:
            raise AuthenticationFailed('The reset link is invalid', 401)

