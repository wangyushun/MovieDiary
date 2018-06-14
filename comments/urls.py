from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_comment, name='post_comment'),
    #path('error/', views.on_error, name='onerror'),
]
