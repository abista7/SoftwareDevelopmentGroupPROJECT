import pycountry
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid


# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=100, null=True)
    alpha_3 = models.CharField(max_length=3, null=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    country_list = []
    for c in list(pycountry.countries):
        country_list.append((c.alpha_2.lower(),c.name))

    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    primary_language = models.ManyToManyField(Language, related_name='primary_language')
    learning_language = models.ManyToManyField(Language, related_name='learning_language')
    gender = models.CharField(choices=GENDERS, max_length=10, default='N/A')
    location = models.CharField(choices=country_list, max_length=2, null=True)
    uuid = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
