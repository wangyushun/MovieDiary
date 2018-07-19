from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from . import models
# Register your models here

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'nickname')

admin.site.register(models.UserProfile, UserProfileAdmin)


# 把扩展内容添加到后台用户管理
class UserProfileInline(admin.StackedInline):
    model = models.UserProfile
    verbose_name_plural = '用户扩展'

class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

