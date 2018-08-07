from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator
from django.conf import settings
from django.contrib.contenttypes.models import ContentType

from . import models
from comments.forms import CommentForm
from comments.models import Comment


# Create your views here.


def get_movies_data(request, movies):
    context = {}
    #分页显示
    paginator = Paginator(movies, settings.MOVIE_LIST_COUNT_PER_PAGE) # Show 2 movies per page
    #页码
    page_list = []
    page = request.GET.get('page', 1)#获取页码参数，没有参数默认为1
    movies_of_page = paginator.get_page(page)
    current_page = movies_of_page.number
    if paginator.num_pages >= 2 :
        page_list = list(range(max(current_page-2, 1), min(current_page+2, paginator.num_pages)+1))
        #是否添加'...'
        if (page_list[0] - 1) >= 2:
            page_list.insert(0, 'left')
            context['left'] = (current_page + 1) // 2
        if (paginator.num_pages - page_list[-1]) >= 2:
            page_list.append('right')
            context['right'] = (current_page + paginator.num_pages) // 2
        #是否添加第1页
        if page_list[0] != 1:
            page_list.insert(0, 1)
        #是否添加第最后一页
        if page_list[-1] != paginator.num_pages:
            page_list.append(paginator.num_pages)
    context['page_list'] = page_list
    context['movies'] = movies_of_page
    return context

def movie(request):  
    '''
    电影列表视图
    '''
    movies = models.Movie.objects.all()
    context = get_movies_data(request, movies)
    context['movie_type'] = models.MovieType.objects.all()
    context['country'] = models.Country.objects.all()
    return render(request, 'movies_list.html', context)


def movie_detail(request, pk):
    '''
    电影详情视图
    '''
    context = {}
    context['movie_type'] = models.MovieType.objects.all()
    context['country'] = models.Country.objects.all()
    context['movie'] = models.Movie.objects.filter(pk=pk).first()
    context['comment_form'] = CommentForm(initial={'content_type': 'movie', 'object_id': pk})
    content_type = ContentType.objects.get_for_model(models.Movie)
    context['comments'] = Comment.objects.filter(content_type=content_type, object_id=pk).all()
    return render(request, 'movie_detail.html', context)

def movie_type(request, pk):
    '''
    电影类型分类电影列表视图
    '''
    movies = models.Movie.objects.filter(movie_type=pk).all()
    context = get_movies_data(request, movies)
    context['movie_type'] = models.MovieType.objects.all()
    context['country'] = models.Country.objects.all()
    context['category'] = models.MovieType.objects.filter(pk=pk).first()#当前分类
    return render(request, 'movies_list.html', context)

def country(request, pk):
    '''
    电影制片国家或地区分类电影列表视图
    '''
    movies = models.Movie.objects.filter(producer_country=pk).all()
    context = get_movies_data(request, movies)
    context['movie_type'] = models.MovieType.objects.all()
    context['country'] = models.Country.objects.all() 
    context['category'] = models.Country.objects.filter(pk=pk).first()#当前分类  
    return render(request, 'movies_list.html', context)

def search(request):
    '''
    搜索电影视图
    '''
    context = {}
    search = request.POST.get('search', '')
    if search == '':
        context['movies'] = []
        context['tvs'] = []
    else:
        movies = models.Movie.objects.filter(name__icontains=search).all()
        context['movies'] = movies
        tvs = models.TVPlay.objects.filter(name__icontains=search).all()
        context['tvs'] = tvs
    context['search'] = search
    return render(request, 'search.html', context)


def tv_play(request):
    '''
    电视剧视图函数
    '''
    type = request.GET.get('type', None)
    if type:
        tvplays = models.TVPlay.objects.filter(movie_type=type).all()
    else:
        tvplays = models.TVPlay.objects.all()
    context = get_movies_data(request, tvplays)
    context['movie_type'] = models.MovieType.objects.all()
    context['country'] = models.Country.objects.all()
    return render(request, 'tv_list.html', context)


def tv_detail(request, pk):
    '''
    电视剧详情视图
    '''
    context = {}
    context['movie_type'] = models.MovieType.objects.all()
    context['country'] = models.Country.objects.all()
    context['movie'] = models.TVPlay.objects.filter(pk=pk).first()
    context['comment_form'] = CommentForm(initial={'content_type': 'tvplay', 'object_id': pk})
    content_type = ContentType.objects.get_for_model(models.TVPlay)
    context['comments'] = Comment.objects.filter(content_type=content_type, object_id=pk).all()
    return render(request, 'movie_detail.html', context)

def tv_type(request, pk):
    '''
    类型分类电视剧列表视图
    '''
    movies = models.TVPlay.objects.filter(movie_type=pk).all()
    context = get_movies_data(request, movies)
    context['movie_type'] = models.MovieType.objects.all()
    context['country'] = models.Country.objects.all()
    context['category'] = models.MovieType.objects.filter(pk=pk).first()#当前分类
    return render(request, 'tv_list.html', context)

def tv_country(request, pk):
    '''
    制片国家或地区分类电视剧列表视图
    '''
    movies = models.TVPlay.objects.filter(producer_country=pk).all()
    context = get_movies_data(request, movies)
    context['movie_type'] = models.MovieType.objects.all()
    context['country'] = models.Country.objects.all() 
    context['category'] = models.Country.objects.filter(pk=pk).first()#当前分类  
    return render(request, 'tv_list.html', context)

