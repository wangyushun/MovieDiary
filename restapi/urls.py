from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views



router = routers.SimpleRouter()
router.register(r'movies', views.MovieViewSet)
router.register(r'countrys', views.CountryViewSet)
router.register(r'languages', views.LanguageViewSet)
router.register(r'movietypes', views.MovieTypeViewSet)
router.register(r'movielines', views.MovieLinesViewSet)
router.register(r'blogs', views.BlogViewSet)
router.register(r'blogtypes', views.BlogTypeViewSet)


urlpatterns = [
    path('', include(router.urls)),
]




