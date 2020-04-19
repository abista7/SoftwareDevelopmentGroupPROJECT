import uuid

import pycountry
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


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
        country_list.append((c.alpha_2.lower(), c.name))

    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    primary_language = models.ManyToManyField(Language, related_name='primary_language')
    learning_language = models.ManyToManyField(Language, related_name='learning_language')
    gender = models.CharField(choices=GENDERS, max_length=10, default='N/A')
    location = models.CharField(choices=country_list, max_length=2, null=True)
    uuid = models.UUIDField(default=uuid.uuid4)
    about_me = models.TextField(default='nothing here', null=True)

    def __str__(self):
        return self.user.username

    def friend_list(self):
        profile_list = []
        query_1 = Friend.objects.filter(profile_1=self)
        for item in query_1:
            if item.is_friend:
                profile_list.append(item.profile_2)

        query_2 = Friend.objects.filter(profile_2=self)
        for item in query_2:
            if item.is_friend:
                profile_list.append(item.profile_1)

        return profile_list

    def get_location_full_name(self):
        if self.location:
            return pycountry.countries.get(alpha_2=self.location.upper()).name
        else:
            return ''

    def get_common_language(self, other):
        my_lang_list = []
        for lang in self.primary_language.all():
            my_lang_list.append(lang)
        for lang in self.learning_language.all():
            my_lang_list.append(lang)
        other_lang_list = []
        for lang in other.primary_language.all():
            other_lang_list.append(lang)
        for lang in other.learning_language.all():
            other_lang_list.append(lang)
        print('function ran')
        return set(my_lang_list) & set(other_lang_list)


class Friend(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    profile_1 = models.ForeignKey(Profile, related_name="friend_creator", on_delete=models.CASCADE)
    profile_2 = models.ForeignKey(Profile, related_name="friend", on_delete=models.CASCADE)
    is_friend = models.BooleanField(default=False)
    friend_time = models.DateTimeField(auto_now=True)


# when a user object gets created (user register) a profile is added automatically
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# when user object gets saved the profile object gets saved
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


def get_profile_model():
    return Profile.objects.filter(user__is_active=True)
