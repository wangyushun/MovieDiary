from imagekit.admin import AdminThumbnail
from xadmin import sites
from xadmin import views as xviews

from .models import (Movie, Country, Language, MovieType, TVPlay)


@sites.register(xviews.BaseAdminView)
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


@sites.register(xviews.CommAdminView)
class AdminSettings(object):
    # 设置base_site.html的Title
    site_title = '电影日记管理后台'
    # 设置base_site.html的Footer
    site_footer = '电影日记'
    menu_style = 'default'



@sites.register(Movie)
class MovieAdmin(object):
    admin_thumbnail = AdminThumbnail(image_field='poster_thumbnail')
    admin_thumbnail.short_description = '海报'


    list_display = ('id', 'admin_thumbnail', 'name', 'director', 'scriptwriter', 'movie_type',
                  'producer_country','language', 'create_datetime', 'grade')
    list_display_links = ('name', 'id')
    
    # 筛选器
    list_filter = ('movie_type', 'producer_country', )  # 过滤器
    search_fields = ('name', 'director', 'scriptwriter')  # 搜索字段
    # reversion_enable = True
 

@sites.register(MovieType)
class MovieTypeAdmin(object):
    list_display = ('id', 'name')
    list_display_links = ('name', 'id')
    
    search_fields = ('name',)  # 搜索字段
    # reversion_enable = True


@sites.register(Country)
class CountryAdmin(object):
    list_display = ('id', 'name')
    list_display_links = ('name', 'id')
    
    search_fields = ('name',)  # 搜索字段
    # reversion_enable = True


@sites.register(Language)
class LanguageAdmin(object):
    list_display = ('id', 'name')
    list_display_links = ('name', 'id')
    
    search_fields = ('name',)  # 搜索字段
    # reversion_enable = True


@sites.register(TVPlay)
class TVPlayAdmin(object):
    admin_thumbnail = AdminThumbnail(image_field='poster_thumbnail')
    admin_thumbnail.short_description = '海报'


    list_display = ('id', 'admin_thumbnail', 'name', 'director', 'scriptwriter', 'movie_type',
                  'producer_country','language', 'create_datetime', 'grade')
    list_display_links = ('name', 'id')
    
    # 筛选器
    list_filter = ('movie_type', 'producer_country', )  # 过滤器
    search_fields = ('name', 'director', 'scriptwriter')  # 搜索字段
    # reversion_enable = True
    

