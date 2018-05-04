from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Country)
admin.site.register(models.Language)
admin.site.register(models.MovieType)

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'director', 'movie_type', 'producer_country',
                    'language', 'create_datetime', 'grade')

admin.site.register(models.Movie, MovieAdmin)

@admin.register(models.MovieLines)
class MovieLinesAdmin(admin.ModelAdmin):
    list_display = ('lines', 'provenance')

