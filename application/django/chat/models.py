from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import Q


class Thread(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='thread_user_1', null=True)
    user2 = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='thread_user_2', null=True)

    def __str__(self):
        return str(self.user1) + ' and ' + str(self.user2) + '\'s thread'

    def get_messages(self):
        return Message.objects.filter(thread=self)

    def get_last_message(self):
        return Message.objects.filter(thread=self).last()

    def get_other_username(self, user):
        if user == self.user1:
            return self.user2.username
        else:
            return self.user1.username


def get_or_create_thread(user1, user2):
    if Thread.objects.filter(Q(user1=user1, user2=user2) | Q(user1=user2, user2=user1)).count() < 1:
        Thread.objects.create(user1=user1, user2=user2)
    return Thread.objects.get(Q(user1=user1, user2=user2) | Q(user1=user2, user2=user1))


def get_thread_by_user(user):
    return Thread.objects.filter(Q(user1=user) | Q(user2=user))


class Message(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='msg_thread_fk')
    body = models.TextField(max_length=640)
