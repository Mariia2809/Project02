from urllib.request import Request

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, DeleteView
from .forms import RegisterUserForm
from .models import Application
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    return render(request, 'index.html')


def profil(request):
    return render(request, 'profil.html')


def login(request):
    return render(request, 'registration/login.html')


def registration(request):
    return render(request, 'registration.html')


class RegisterView(CreateView):
    template_name = 'registration.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')


def validate_username(request):
    username = request.GET.get('username', None)
    response = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(response)


class BBLogoutView(LogoutView):
    success_url = reverse_lazy('index')


class ApplicationListView(generic.ListView):
    model = Application
    template_name = 'index.html'
    context_object_name = 'applications'


class ApplicationsByUserListView(LoginRequiredMixin, generic.ListView):
    model = Application
    template_name = 'profil.html'
    context_object_name = 'applications'

    def get_queryset(self):
        return Application.objects.filter(user=self.request.user)


class ApplicationDelete(ApplicationListView):
    model = Application
    context_object_name = 'application'
    template_name = 'deleting.html'
    success_url = reverse_lazy('request')


class MyPostListViews(generic.ListView):
    model = Application
    context_object_name = 'application'
    template_name = 'request.html'

    def get_queryset(self):
        return Application.object.filter(user=self.request.user).object_by('-date')


class ApplicationCreate(LoginRequiredMixin, CreateView):
    model = Application
    fields = ['title', 'category', 'photo_file']
    template_name = 'request.html'
    success_url = reverse_lazy('request')


def request_catalog(request):
    return render(request, "request.html")


def add_request(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        request.objects.create(title=title, description=description)
        return redirect('list_requests')
    return render(request, 'request.html')


