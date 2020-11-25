from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView

from .forms import CustomUserCreationForm, UserForm
from .models import CustomUser


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


def lk_view(request, *args, **kwargs):
    account = CustomUser.objects.all()
    context = {'account': account}
    return render(request, 'lk.html', context)


class LkDetailView(DetailView):
    model = CustomUser
    template_name = 'lk/detail_lk_view.html'
    context_object_name = 'user_lk'
