# chat/views.py
from django.shortcuts import render

from mainapp.models import get_profile_model
from .models import get_or_create_thread, Message


def room(request, other_profile_uuid=''):
    other_profile = get_profile_model().get(uuid=other_profile_uuid)
    thread = get_or_create_thread(user1=request.user, user2=other_profile.user)
    messages = Message.objects.filter(thread=thread)
    context = {'room_name': thread.id, 'messages': messages}
    return render(request, 'chat/room.html', context)
