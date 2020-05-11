# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('<uuid:other_profile_uuid>/', views.room, name='room'),
]
