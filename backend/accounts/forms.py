from django import forms
from django.contrib.auth.forms import UserCreationForm
from allauth.account.forms import SignupForm
from .models import CustomUser

class CustomUserCreateForm(SignupForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password1', 'password2']
