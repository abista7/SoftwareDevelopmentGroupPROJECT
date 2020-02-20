from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('arjun', views.arjun, name='arjun'),
    path('mariam', views.mariam, name='mariam'),
    path('ryan', views.ryan, name='ryan'),
    path('sawara', views.sawara, name='sawara'),
    path('dylan', views.dylan, name='dylan'),
    path('cassie', views.dylan, name='cassie'),
]
