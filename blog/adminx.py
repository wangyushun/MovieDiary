from xadmin import sites

from .models import Blog, BlogTag, BlogType


@sites.register(BlogTag)
class BlogTagAdmin(object):
    list_display = ('id', 'name')
    list_display_links = ('name', 'id')
    
    search_fields = ('name',)  # 搜索字段
    # reversion_enable = True


@sites.register(BlogType)
class BlogTypeAdmin(object):
    list_display = ('id', 'name')
    list_display_links = ('name', 'id')
    
    search_fields = ('name',)  # 搜索字段
    # reversion_enable = True


@sites.register(Blog)
class BlogAdmin(object):
    list_display = ('id', 'title', 'author', 'post_by', 'blog_type', 'blog_tags', 'create_time')
    list_display_links = ('id', 'title')
    
    # 筛选器
    list_filter = ('blog_type', 'blog_tags', )  # 过滤器
    search_fields = ('title', 'author')  # 搜索字段
    # reversion_enable = True




