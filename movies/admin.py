from django.contrib import admin
from imagekit.admin import AdminThumbnail
from . import models

# Register your models here.

admin.site.register(models.Country)
admin.site.register(models.Language)
admin.site.register(models.MovieType)

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'admin_thumbnail', 'name', 'director', 'movie_type', 'producer_country',
                    'language', 'create_datetime', 'grade')

    admin_thumbnail = AdminThumbnail(image_field='poster_thumbnail')


class MovieLinesAdmin(admin.ModelAdmin):
    list_display = ('lines', 'provenance')

admin.site.register(models.Movie, MovieAdmin)
admin.register(models.MovieLines, MovieLinesAdmin)

