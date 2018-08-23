from django.db import models
from django.core import validators
from django.utils import timezone
from django.urls import reverse, NoReverseMatch

#from ckeditor.fields import RichTextField 
from ckeditor_uploader.fields import RichTextUploadingField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.

class MovieType(models.Model):
    '''
    电影类型
    '''
    name = models.CharField(max_length=25, verbose_name='电影类型名字')

    class Meta:
        verbose_name = '电影类型'
        verbose_name_plural = '电影类型'

    def __str__(self):
        return self.name

class Language(models.Model):
    '''
    语言
    '''
    name = models.CharField(max_length=25, verbose_name='语言名字')

    class Meta:
        verbose_name = '语言'
        verbose_name_plural = '语言'

    def __str__(self):
        return self.name

class Country(models.Model):
    '''
    地区国家
    '''
    name = models.CharField(max_length=25, verbose_name='国家/地区名字')

    class Meta:
        verbose_name = '国家/地区'
        verbose_name_plural = '国家/地区'

    def __str__(self):
        return self.name


class Movie(models.Model):
    poster = models.ImageField(verbose_name='海报', upload_to='poster', blank=True, default='', null=True)#海报
    poster_thumbnail = ImageSpecField(source='poster',
                                      processors=[ResizeToFill(200, 300)],
                                      format='JPEG',
                                      options={'quality': 60})
    name = models.CharField(verbose_name='名字', max_length=25)#电影名
    director = models.CharField(verbose_name='导演', max_length=50, default='不详')#导演
    scriptwriter = models.CharField(verbose_name='编剧', max_length=100, default='不详')
    actor = models.CharField(verbose_name='主演', max_length=100, default='')#演员
    movie_type = models.ManyToManyField(to='MovieType', verbose_name='类型', related_name='movie_type')#电影类型
    producer_country = models.ManyToManyField(to='Country', verbose_name='制片国家', related_name='producer_country')#制片国家
    language = models.ManyToManyField(to='Language', verbose_name='语言', related_name='language')#语言
    release_date = models.DateField(verbose_name='上映日期')#上映日期
    release_country = models.ForeignKey(to='Country', verbose_name='上映国家', related_name='release_country',
                                        on_delete=models.DO_NOTHING)#上映国家
    time_length = models.IntegerField(verbose_name='片长', default=0)#单位分钟
    grade = models.DecimalField(verbose_name='评分', max_digits=3, decimal_places=1, 
                                validators=[validators.MaxValueValidator(10.0), validators.MinValueValidator(0.0)],
                                default=0)#评分
    trailer_link = models.CharField(verbose_name='预告片连接', max_length=250, blank=True, default='')
    synopsis = RichTextUploadingField(verbose_name='剧情简介', default='')#剧情简介
    create_datetime = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)#日记创建日期
    resource = RichTextUploadingField(verbose_name='资源', blank=True, default='')


    def __str__(self):
        return '<Movie>:{0}'.format(self.name)

    def get_detail_url(self):
        try:
            url = reverse('movie')
        except NoReverseMatch:
            url = None 
        else:
            url = url + str(self.pk)
        return url

    class Meta:
        ordering = ['-create_datetime']#按日期倒序排序
        verbose_name = '电影'
        verbose_name_plural = '电影'


class MovieLines(models.Model):
    '''
    经典电影台词
    '''
    lines = models.TextField()#台词
    provenance = models.CharField(max_length=20)#出处

    def __str__(self):
        return '<MovieLines>:{0}--<<{1}>>'.format(self.lines, self.provenance)

    class Meta:
        verbose_name = '电影台词'
        verbose_name_plural = '电影台词'
    

class TVPlay(models.Model):
    poster = models.ImageField(verbose_name='海报', upload_to='poster', default='', null=True)#海报
    poster_thumbnail = ImageSpecField(source='poster',
                                      processors=[ResizeToFill(200, 300)],
                                      format='JPEG',
                                      options={'quality': 60})
    name = models.CharField(verbose_name='名字', max_length=25)#电影名
    director = models.CharField(verbose_name='导演', max_length=25, default='不详')#导演
    scriptwriter = models.CharField(verbose_name='编剧', max_length=50, default='不详')
    actor = models.CharField(verbose_name='主演', max_length=50, default='')#演员
    movie_type = models.ManyToManyField(to='MovieType', verbose_name='类型', related_name='tv_movie_type')#电影类型
    producer_country = models.ManyToManyField(to='Country', verbose_name='制片国家', related_name='tv_producer_country')#制片国家
    language = models.ManyToManyField(to='Language', verbose_name='语言', related_name='tv_language')#语言
    release_date = models.DateField(verbose_name='上映日期')#上映日期
    release_country = models.ForeignKey(to='Country', verbose_name='上映国家', related_name='tv_release_country',
                                        on_delete=models.DO_NOTHING)#上映国家
    season = models.IntegerField(verbose_name='第n季', default=0)
    episode_num = models.IntegerField(verbose_name='集数', default=0)
    time_length = models.IntegerField(verbose_name='片长', default=0)#单位分钟
    grade = models.DecimalField(verbose_name='评分', max_digits=3, decimal_places=1, 
                                validators=[validators.MaxValueValidator(10.0), validators.MinValueValidator(0.0)],
                                default=0)#评分
    synopsis = RichTextUploadingField(verbose_name='剧情简介', default='')#剧情简介
    create_datetime = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)#日记创建日期
    resource = RichTextUploadingField(verbose_name='资源', blank=True, default='')

    def __str__(self):
        return '<TVPlay>:{0}'.format(self.name)

    def get_detail_url(self):
        try:
            url = reverse('tvplay')
        except NoReverseMatch:
            url = None 
        else:
            url = url + str(self.pk)
        return url

    class Meta:
        ordering = ['-create_datetime']#按日期倒序排序
        verbose_name = '电视剧'
        verbose_name_plural = '电视剧'

