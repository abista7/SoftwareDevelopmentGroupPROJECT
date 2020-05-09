from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Post


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=32)
    last_name = forms.CharField(max_length=32)
    email = forms.EmailField(max_length=64)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']


class PostForm(forms.ModelForm):
    description = forms.CharField(max_length=255)
    image = forms.ImageField(required=False)

    class Meta:
        model = Post
        labels = {
            'image': 'Image',
            'description': 'Description'
        }
        fields = ['image', 'description']
