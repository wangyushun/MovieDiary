from django.db import models
from django.core import validators
#from django.utils import timezone
#from ckeditor.fields import RichTextField 
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class MovieType(models.Model):
    '''
    电影类型
    '''
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Language(models.Model):
    '''
    语言
    '''
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Country(models.Model):
    '''
    地区国家
    '''
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Movie(models.Model):
    poster = models.ImageField(upload_to='poster', default='', null=True)#海报
    name = models.CharField(max_length=25)#电影名
    director = models.CharField(max_length=25, default='')#导演
    actor = models.CharField(max_length=25, default='')#演员
    movie_type = models.ForeignKey('MovieType', on_delete=models.DO_NOTHING)#电影类型
    producer_country = models.ForeignKey('Country', on_delete=models.DO_NOTHING)#制片国家
    language = models.ForeignKey('Language', on_delete=models.DO_NOTHING)#语言
    release_date = models.DateField()#上映日期
    release_country = models.CharField(max_length=20)#上映国家
    time_length = models.IntegerField(default=0)#时长，单位分钟
    grade = models.DecimalField(max_digits=3, decimal_places=1, 
                                validators=[validators.MaxValueValidator(10.0), validators.MinValueValidator(0.0)],
                                default=0)#评分
    synopsis = RichTextUploadingField(default='')#剧情简介
    create_datetime = models.DateTimeField(auto_now_add=True)#日记创建日期

    def __str__(self):
        return '<Movie>:{0}'.format(self.name)

    class Meta:
        ordering = ['-create_datetime']#按日期倒序排序


class MovieLines(models.Model):
    '''
    经典电影台词
    '''
    lines = models.TextField()#台词
    provenance = models.CharField(max_length=20)#出处

    def __str__(self):
        return '<MovieLines>:{0}--<<{1}>>'.format(self.lines, self.provenance)
    


