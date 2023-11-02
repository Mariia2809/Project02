from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

def home(request):
    # Обработка главной страницы
    return render(request, 'design/index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('user_dashboard') # Перенаправление на личный кабинет после входа
    else:
# Обработка неправильных данных входа
        return render(request, 'design/registration.html', {'error_message': 'Неправильное имя пользователя или пароль.'})

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_dashboard') # Перенаправление на личный кабинет после регистрации
    else:
        form = UserCreationForm()
    return render(request, 'registration.html')