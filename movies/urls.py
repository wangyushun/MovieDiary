from django.contrib import admin
from django.urls import path, re_path
from . import views
from . import rss

urlpatterns = [
    path('', views.movie, name='movie'),
    path('<int:pk>', views.movie_detail, name='movie_detail'),
    path('movie_type/<int:pk>', views.movie_type, name='movie_type'),
    path('country/<int:pk>', views.country, name='country'),
    path('search/', views.search, name='search'),
    path('rss/', rss.AllMoviesRssFeed(), name='rss'),
    path('tv/', views.tv_play, name='tvplay'),
    path('tv/<int:pk>', views.tv_detail, name='tv_detail'),
    path('tv/type/<int:pk>', views.tv_type, name='tv_type'),
    path('tv/country/<int:pk>', views.tv_country, name='tv_country'),
]