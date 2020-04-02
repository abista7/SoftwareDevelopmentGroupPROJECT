from django.db import models


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

    name = models.CharField(max_length=100)
    email = models.EmailField()
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
    profile_picture = models.URLField(default='https://i.imgur.com/OYQulGk.png')
