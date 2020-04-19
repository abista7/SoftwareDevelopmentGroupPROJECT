from django.urls import path
import uuid

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<uuid:profile_uuid>/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('settings/',views.settings, name='settings'),
    path('friends/', views.friends, name='friends')
]
