from django.contrib import admin
from . import models
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
	display = ['username', 'context', 'create_time']

admin.site.register(models.Comment, CommentAdmin)
