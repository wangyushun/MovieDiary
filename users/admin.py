from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from . import models
# Register your models here

class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'nickname')

admin.site.register(models.Profile, ProfileAdmin)


# 把扩展内容添加到后台用户管理
class ProfileInline(admin.StackedInline):
    model = models.Profile
    verbose_name_plural = '用户扩展'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

