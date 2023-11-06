from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView
from .forms import RegisterUserForm
from .models import Application
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
class ApplicationListView(generic.ListView):
    model = Application
    paginate_by = 4
    template_name = 'base.html'