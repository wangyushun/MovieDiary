from xadmin import sites
from xadmin import views as xviews

from .models import Comment


@sites.register(Comment)
class CommentAdmin(object):
    def content_object_name(self, obj):
        return obj.content_object.name

    content_object_name.short_description = '被评论者'

    list_display = ('id', 'content_object_name', 'content_type', 'user', 'context', 'create_time')
    list_display_links = ('name', 'id')
    
    # 筛选器
    list_filter = ('content_type',)  # 过滤器
    search_fields = ('user', 'context')  # 搜索字段
    # reversion_enable = True




