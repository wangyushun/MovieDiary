from xadmin import sites

from .models import UserProfile


@sites.register(UserProfile)
class UserProfileAdmin(object):
    list_display = ('id', 'user', 'nickname')
    list_display_links = ('id', 'nickname')

    search_fields = ('nickname',)  # 搜索字段
    # reversion_enable = True

