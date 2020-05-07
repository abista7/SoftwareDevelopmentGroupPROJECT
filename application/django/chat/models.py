from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import Q


class Tread(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='tread_user_1', null=True)
    user2 = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='tread_user_2', null=True)

    def get_or_create_thread(self, user2):
        if Tread.objects.filter(Q(self=self, user2=user2) | Q(self=user2, user2=self)).count() < 1:
            Tread.objects.create(self=self, user2=user2)
        return Tread.objects.filter(Q(self=self, user2=user2) | Q(self=user2, user2=self))

    def get_messages(self):
        return Message.objects.filter(tread=self)


class Message(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    tread = models.ForeignKey(Tread, on_delete=models.CASCADE)
    body = models.TextField()
