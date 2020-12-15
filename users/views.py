from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import CustomUser
from .forms import CustomUserCreationForm, UserForm
from .serializers import CustomUserSerializer, UserRegistrSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView


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

