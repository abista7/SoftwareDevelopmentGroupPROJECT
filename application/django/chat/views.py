# chat/views.py
from django.shortcuts import render

from mainapp.models import get_profile_model
from .models import get_or_create_thread


def chat(request):
    return render(request, 'chat/index.html', {})


def room(request, other_profile_uuid):
    other_profile = get_profile_model().get(uuid=other_profile_uuid)
    thread = get_or_create_thread(user1=request.user, user2=other_profile.user)
    return render(request, 'chat/room.html', {
        'room_name': thread.id
    })
