from django.contrib import admin
from . import models

admin.site.site_header = '电影日记管理系统'
admin.site.site_title = '电影日记'

# Register your models here.
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'blog_type', 'blog_tags_disp', 'create_time')

    def blog_tags_disp(self, obj):
        return [item.name for item in obj.blog_tags.all()]

    blog_tags_disp.short_description = '博客标签' #admin后台此字段表列显示名称，等价于模型字段verbose_name参数

    # 多对多字段编辑方式
    filter_horizontal = ['blog_tags',]
    # 筛选器
    list_filter = ('blog_type', 'blog_tags',)  # 过滤器
    search_fields = ('title', 'author')  # 搜索字段
    date_hierarchy = 'create_time'  # 详细时间分层筛选


class BlogTagAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(models.BlogType, BlogTypeAdmin)
admin.site.register(models.Blog, BlogAdmin)
admin.site.register(models.BlogTag, BlogTagAdmin)

