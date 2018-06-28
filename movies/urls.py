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
]