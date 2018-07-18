from django.contrib import admin
from . import models

# Register your models here.
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'blog_type', 'blog_tags_disp', 'create_time')

    def blog_tags_disp(self, obj):
        return [item.name for item in obj.blog_tags.all()]

    blog_tags_disp.short_description = '博客标签' #admin后台此字段表列显示名称，等价于模型字段verbose_name参数



class BlogTagAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(models.BlogType, BlogTypeAdmin)
admin.site.register(models.Blog, BlogAdmin)
admin.site.register(models.BlogTag, BlogTagAdmin)
