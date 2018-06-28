from collections import OrderedDict

from django.shortcuts import render, get_object_or_404, Http404
from django.core.paginator import Paginator
from django.conf import settings

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from movies.models import Movie, Country, Language, MovieType, MovieLines
from blog.models import Blog, BlogType
from . import serializers

# Create your views here.


class DefaultPagination(PageNumberPagination): 
    '''
    配置列表视图的分页
    ''' 
    page_size = 20 
    page_size_query_param = 'page_size'  
    page_query_param = "page"  
    max_page_size = 100 



class CustomPagination(PageNumberPagination): 
    '''
    自定义列表视图的分页，返回数据格式
    ''' 
    page_size = 2 
    page_size_query_param = 'page_size'  
    page_query_param = "page"  
    max_page_size = 100 

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('num_pages', self.page.paginator.num_pages),#总页数
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data),
            ('page_links', self.get_html_context()),#页码表连接
            ('page_html', self.to_html())       #页码表html
        ]))


class MovieViewSet(viewsets.ModelViewSet):
    """
    电影视图集
    API endpoint that allows movies to be viewed or edited.
    """
    queryset = Movie.objects.all().order_by('-create_datetime')
    serializer_class = serializers.MovieSerializer
    pagination_class = CustomPagination 

    #检索某一部电影详情
    def retrieve(self, request, pk=None):
        try:
            pk = int(pk)
        except ValueError:
            raise Http404("Movie does not exist")
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieDetailSerializer(movie, context={'request': request})

        return Response(serializer.data)


class BlogViewSet(viewsets.ModelViewSet):
    """
    博客视图集
    API endpoint that allows blogs to be viewed or edited.
    """
    queryset = Blog.objects.all().order_by('-create_time')
    serializer_class = serializers.BlogSerializer
    pagination_class = CustomPagination 


class CountryViewSet(viewsets.ModelViewSet):
    """
    国家/地区视图集
    API endpoint that allows countrys to be viewed or edited.
    """
    queryset = Country.objects.all()
    serializer_class = serializers.CountrySerializer
    pagination_class = DefaultPagination 



class LanguageViewSet(viewsets.ModelViewSet):
    """
    语言视图集
    API endpoint that allows languages to be viewed or edited.
    """
    queryset = Language.objects.all()
    serializer_class = serializers.LanguageSerializer
    pagination_class = DefaultPagination 



class MovieTypeViewSet(viewsets.ModelViewSet):
    """
    电影类型视图集
    API endpoint that allows movietypes to be viewed or edited.
    """
    queryset = MovieType.objects.all()
    serializer_class = serializers.MovieTypeSerializer
    pagination_class = DefaultPagination 


class MovieLinesViewSet(viewsets.ModelViewSet):
    """
    电影类型视图集
    API endpoint that allows MovieLines to be viewed or edited.
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)#未经认证的用户只允许读
    queryset = MovieLines.objects.all()
    serializer_class = serializers.MovieLinesSerializer
    pagination_class = DefaultPagination 


class BlogTypeViewSet(viewsets.ModelViewSet):
    """
    博客类型视图集
    API endpoint that allows blogtypes to be viewed or edited.
    """
    queryset = BlogType.objects.all()
    serializer_class = serializers.BlogTypeSerializer
    pagination_class = DefaultPagination


