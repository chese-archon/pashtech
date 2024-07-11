from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), #home
    path('home/', views.home, name='home'), #home
    path('audio/', views.audio, name='audio'),
    path('video/', views.video, name='video'),
    path('afisha/', views.afisha, name='afisha'),
    path('news/', views.news, name='news'),
    path('bio/', views.bio, name='bio'),
    path('contacts/', views.contacts, name='contacts'),
]