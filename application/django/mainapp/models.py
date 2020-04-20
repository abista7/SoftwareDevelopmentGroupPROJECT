from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
import pycountry

from django.conf import settings

# Create your models here.

class Profile(models.Model):

    LANGUAGE_CHOICES = [
        ('English', 'English'),
        ('Spanish', 'Spanish'),
        ('German', 'German'),
        ('French', 'French')
    ]

    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    name = models.CharField(max_length=100, default=None)
    primary_language = models.CharField(
        max_length=100,
        choices=LANGUAGE_CHOICES,
        default='English'
    )
    learning_language = models.CharField(
        max_length=100,
        choices=LANGUAGE_CHOICES,
        default='English'
    )
    gender = models.CharField(choices=GENDERS, max_length=10, default='N/A')
    location = models.CharField(max_length=100, default='Earth')
    email = models.EmailField(default=None)
    profile_picture = models.URLField(default='https://i.imgur.com/OYQulGk.png')
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)


class Post(models.Model):
    description = models.CharField(max_length=200)
    created_at= models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)



