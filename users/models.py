from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='用户')
    nickname = models.CharField(max_length=20, default='', verbose_name='昵称')

    def __str__(self):
        return '<UserProfile:{0}>'.format(self.nickname)

    class Meta:
        verbose_name_plural = '用户扩展'



