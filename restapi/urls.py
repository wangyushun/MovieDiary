from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views



router = routers.SimpleRouter()
router.register(r'movies', views.MovieViewSet)
# router.register(r'movies/(?P<pk>[^/.]+)/$', views.MovieDetailViewSet)


urlpatterns = [
    path('', include(router.urls)),
    #path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]




