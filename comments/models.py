from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

# Create your models here.

class Comment(models.Model):
    content_type = models.ForeignKey(ContentType,verbose_name='评论对象类型', on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(verbose_name='评论对象id')
    content_object = GenericForeignKey('content_type', 'object_id')

    user = models.ForeignKey(User, verbose_name='评论者', related_name='user', on_delete=models.CASCADE)  
    context = models.TextField(verbose_name='评论内容', default='')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')
    # reply_to = models.ForeignKey(User, null='True', related_name='reply_to', on_delete=models.CASCADE)

    def __str__(self):
        return self.context

    class Meta:
        ordering = ['-create_time'] #时间倒序
        verbose_name = '评论'
        verbose_name_plural = '评论'


