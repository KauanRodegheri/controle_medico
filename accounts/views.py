from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate


def register_view(request):
    if request.method == 'POST':
        user = UserCreationForm(request.POST)
        if user.is_valid():
            user.save()
            return redirect('login')
    else:
        user = UserCreationForm()
    return render(request, 'register.html', {'register_form': user})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('home_view')
    else:
        login_form = AuthenticationForm()
    return render(request, 'login.html', {'login_form': login_form})

def logout_view(request):
    logout(request)
    return redirect('home_view')
