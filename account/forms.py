from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
        class Meta:
                model = CustomUser
                fields = ('email', 'username', 'password1', 'password2')

class CustomUserAuthenticationForm(AuthenticationForm):
        username = forms.EmailField(max_length=254)
class Meta:
        model = CustomUser
        fields = ('username', 'password')