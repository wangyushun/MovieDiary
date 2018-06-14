from django.shortcuts import render, get_object_or_404, Http404
from rest_framework import viewsets
from rest_framework.response import Response

from django.core.paginator import Paginator
from django.conf import settings
from movies.models import Movie
from .serializers import MovieSerializer, MovieDetailSerializer

# Create your views here.


def get_movies_data(request, movies):
    context = {}
    #分页显示
    paginator = Paginator(movies, settings.MOVIE_LIST_COUNT_PER_PAGE) # Show 2 movies per page
    page = request.GET.get('page', 1)#获取页码参数，没有参数默认为1
    try:
        page = int(page)
    except ValueError:
        raise Http404("ValueError")
    
    if not (0< page <= paginator.num_pages):
        return {} 
    else:  
        movies_of_page = paginator.get_page(page)  
        return movies_of_page


class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows movies to be viewed or edited.
    """
    queryset = Movie.objects.all().order_by('-create_datetime')
    serializer_class = MovieSerializer

    #获取指定页的电影列表
    def list(self, request):
        movies = get_movies_data(request, self.queryset)
        serializer = MovieSerializer(movies, many=True, context={'request': request})
        return Response(serializer.data)

    #检索某一部电影详情
    def retrieve(self, request, pk=None):
        try:
            pk = int(pk)
        except ValueError:
            raise Http404("Movie does not exist")
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieDetailSerializer(movie, context={'request': request})
        return Response(serializer.data)





