from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from .forms import CustomUserAuthenticationForm, CustomUserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


# Logout View
def logout_view(request):
    logout(request)
    return redirect('home')

# Home View
def home_view(request):
    return render(request, 'home.html')

# Register View
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

# Login View with Admin Redirect
def login_view(request):
    if request.method == 'POST':
        form = CustomUserAuthenticationForm(request, data=request.POST)  
        if form.is_valid():
            email = form.cleaned_data.get('username')  
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)  
            if user is not None:
                login(request, user)
                # Check if the user is an admin
                if user.is_staff or user.is_superuser:
                    return redirect('admin_dashboard')  # Redirect to admin dashboard
                else:
                    return redirect('home')  # Redirect to regular home page
    else:
        form = CustomUserAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})





# Admin Dashboard View

def admin_dashboard(request):
    users_count = User.objects.count()  # Total users
    admins_count = User.objects.filter(is_admin=True).count()  # Admins
    regular_users_count = users_count - admins_count  # Regular users

    users = User.objects.all()  # List of all users

    context = {
        'users_count': users_count,
        'admins_count': admins_count,
        'regular_users_count': regular_users_count,
        'users': users,
    }
    return render(request, 'accounts/admin_dashboard.html', context)
