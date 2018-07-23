from django.contrib import admin
from imagekit.admin import AdminThumbnail
from . import models

# Register your models here.

admin.site.register(models.Country)
admin.site.register(models.Language)
admin.site.register(models.MovieType)

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'admin_thumbnail', 'name', 'director', 'scriptwriter', 'movie_type_list',
                    'producer_country_list','language_list', 'create_datetime', 'grade', 'resource')

    admin_thumbnail = AdminThumbnail(image_field='poster_thumbnail')
    admin_thumbnail.short_description = '海报'

    # 显示多对多字段, 定义一个方法，遍历，然后用列表返回
    # Field producer_country 
    def producer_country_list(self, obj):
        return [item.name for item in obj.producer_country.all()]

    producer_country_list.short_description = '制片国家' #admin后台此字段表列显示名称，等价于模型字段verbose_name参数

    # Field language 
    def language_list(self, obj):
        return [item.name for item in obj.language.all()]

    language_list.short_description = '语言'

    # Field movie_type 
    def movie_type_list(self, obj):
        return [item.name for item in obj.movie_type.all()]

    movie_type_list.short_description = '类型'



class MovieLinesAdmin(admin.ModelAdmin):
    list_display = ('lines', 'provenance')


class TVPlayAdmin(MovieAdmin):
    list_display = MovieAdmin.list_display + ('season', 'episode_num')


admin.site.register(models.Movie, MovieAdmin)
admin.site.register(models.MovieLines, MovieLinesAdmin)
admin.site.register(models.TVPlay, TVPlayAdmin)

