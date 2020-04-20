from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<int:profile_id>/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('', include("django.contrib.auth.urls")),
    path('homepage/', views.homepage, name='home'),
]