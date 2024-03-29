from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

from django.contrib.auth.forms import AuthenticationForm

from django.forms.widgets import PasswordInput, TextInput

from django import forms

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput())
    password = forms.CharField(label="Password", max_length=30, widget=forms.PasswordInput())
