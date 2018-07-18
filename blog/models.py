from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class BlogType(models.Model):
    name = models.CharField(verbose_name='类型名称', max_length=20, default='杂谈')

    class Meta:
        verbose_name = '博客类型'
        verbose_name_plural = '博客类型'

    def __str__(self):
        return self.name


class BlogTag(models.Model):
    name = models.CharField(verbose_name='标签名称', max_length=20, default='')

    class Meta:
        verbose_name = '博客标签'
        verbose_name_plural = '博客标签'

    def __str__(self):
        return self.name



class Blog(models.Model):
    '''
    Blog Model
    '''
    title = models.CharField(verbose_name='标题', max_length=50, default='无题')
    text = RichTextUploadingField(verbose_name='内容', )
    blog_type = models.ForeignKey(to='BlogType', verbose_name='类型', related_name='blog_type', null=True, on_delete=models.SET_NULL)#当外键删除时设置为Null
    blog_tags = models.ManyToManyField(to='BlogTag', verbose_name='标签', related_name='blog_tags')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)#创建时自动添加当前时间
    modified_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)#修改保存时更新时间
    author = models.CharField(verbose_name='作者', max_length=50, default='')
    post_by = models.ForeignKey(User, verbose_name='发布者', null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['-create_time']
        verbose_name = '博客' #下面2行用于Admin后台显示模型中文名
        verbose_name_plural = '博客'

    def __str__(self):
        return '<Blog>:{0}'.format(self.title)


