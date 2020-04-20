<<<<<<< HEAD
from django.urls import path, include
=======
from django.urls import path
import uuid
>>>>>>> origin/dev-ryan

from . import views

urlpatterns = [
    path('', views.index, name='index'),
<<<<<<< HEAD
    path('profile/<int:profile_id>/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('', include("django.contrib.auth.urls")),
    path('homepage/', views.homepage, name='home'),
]
=======
    path('profile/<uuid:profile_uuid>/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('settings/',views.settings, name='settings'),
    path('friends/', views.friends, name='friends')
]
>>>>>>> origin/dev-ryan
