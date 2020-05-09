# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.chat, name='chat'),
    path('<uuid:other_profile_uuid>/', views.room, name='room'),
]
