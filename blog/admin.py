from django.contrib import admin
from . import models

# Register your models here.
class BlogTypeAdmin(admin.ModelAdmin):
	list_display = ('name',)


class BlogAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'blog_type', 'create_time')


admin.site.register(models.BlogType, BlogTypeAdmin)
admin.site.register(models.Blog, BlogAdmin)

