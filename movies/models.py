from django.db import models
from django.core import validators
#from django.utils import timezone
#from ckeditor.fields import RichTextField 
from ckeditor_uploader.fields import RichTextUploadingField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

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
    poster = models.ImageField(verbose_name='电影海报', upload_to='poster', default='', null=True)#海报
    poster_thumbnail = ImageSpecField(source='poster',
                                      processors=[ResizeToFill(200, 300)],
                                      format='JPEG',
                                      options={'quality': 60})
    name = models.CharField(verbose_name='电影名字', max_length=25)#电影名
    director = models.CharField(verbose_name='导演', max_length=25, default='')#导演
    actor = models.CharField(verbose_name='主演', max_length=25, default='')#演员
    movie_type = models.ForeignKey(to='MovieType', verbose_name='电影类型', on_delete=models.DO_NOTHING)#电影类型
    producer_country = models.ForeignKey(to='Country', verbose_name='制片国家', related_name='producer_country',
                                        on_delete=models.DO_NOTHING)#制片国家
    language = models.ForeignKey(to='Language', verbose_name='语言', on_delete=models.DO_NOTHING)#语言
    release_date = models.DateField(verbose_name='上映日期')#上映日期
    #release_country = models.CharField(verbose_name='上映国家', max_length=20)#上映国家
    release_country = models.ForeignKey(to='Country', verbose_name='上映国家', related_name='release_country',
                                        on_delete=models.DO_NOTHING)#上映国家
    time_length = models.IntegerField(verbose_name='电影时长', default=0)#时长，单位分钟
    grade = models.DecimalField(verbose_name='电影评分', max_digits=3, decimal_places=1, 
                                validators=[validators.MaxValueValidator(10.0), validators.MinValueValidator(0.0)],
                                default=0)#评分
    synopsis = RichTextUploadingField(verbose_name='剧情简介', default='')#剧情简介
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
    


