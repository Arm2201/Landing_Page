from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserAuthenticationForm, CustomUserCreationForm

def logout_view(request):
    logout(request)
    return redirect('home')

def home_view(request):
    return render(request, 'home.html')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home') 
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomUserAuthenticationForm(request, data=request.POST)  
        if form.is_valid():
            email = form.cleaned_data.get('username')  
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)  
            if user is not None:
                login(request, user)
                return redirect('home') 
    else:
        form = CustomUserAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})
