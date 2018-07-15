from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='用户')
    nickname = models.CharField(max_length=20, default='', verbose_name='昵称')

    class Meta:
        verbose_name_plural = '用户扩展'



