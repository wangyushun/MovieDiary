from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator
from django.conf import settings
from . import models


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
    return render(request, 'movie_detail.html', context)

def movie_type(request, pk):
    '''
    电影类型分类电影列表视图
    '''
    movies = models.Movie.objects.filter(movie_type=pk).all()
    context = get_movies_data(request, movies)
    context['movie_type'] = models.MovieType.objects.all()
    context['country'] = models.Country.objects.all()
    
    return render(request, 'movies_list.html', context)

def country(request, pk):
    '''
    电影制片国家或地区分类电影列表视图
    '''
    movies = models.Movie.objects.filter(producer_country=pk).all()
    context = get_movies_data(request, movies)
    context['movie_type'] = models.MovieType.objects.all()
    context['country'] = models.Country.objects.all()   
    return render(request, 'movies_list.html', context)

def search(request):
    '''
    搜索电影视图
    '''
    search = request.POST.get('search', '')
    movies = models.Movie.objects.filter(name__icontains=search).all()
    context = get_movies_data(request, movies)
    context['movie_type'] = models.MovieType.objects.all()
    context['country'] = models.Country.objects.all()
    return render(request, 'movies_list.html', context)





