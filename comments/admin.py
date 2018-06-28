from django.contrib import admin
from . import models
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
	list_display = ('content_object', 'user', 'create_time', 'content_type', 'context')
	

admin.site.register(models.Comment, CommentAdmin)
