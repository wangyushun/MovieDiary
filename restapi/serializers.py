import os
from lxml import etree, html

from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone

from rest_framework import serializers

from movies.models import Language, Country, Movie, MovieType, MovieLines
from blog.models import Blog, BlogType


def html_str_img_build_absolute_uri(request, html):
    '''
    html字符串中的img标签src属性转为全路径
    '''
    if not html:
        return ''
    # tree = etree.fromstring(html)
    tree = etree.HTML(html)
    imgs = tree.xpath("//img")
    for img in imgs:
        src = img.get('src')
        #如果src是相对路径，转为全路径，从新设置src属性
        if not src.startswith('http://'):
            uri = request.build_absolute_uri(src)
            img.set('src', uri)
            
    return etree.tostring(tree, encoding = "utf-8", pretty_print = True, method = "html")


class LanguageSerializer(serializers.ModelSerializer):
    '''
    语言模型序列化
    '''
    class Meta:
        model = Language
        fields = ('id', 'name')


class CountrySerializer(serializers.ModelSerializer):
    '''
    国家/地区模型序列化
    '''
    class Meta:
        model = Country
        fields = ('id', 'name')

class MovieTypeSerializer(serializers.ModelSerializer):
    '''
    电影类型模型序列化
    '''
    class Meta:
        model = MovieType
        fields = ('id', 'name')


class MovieLinesSerializer(serializers.ModelSerializer):
    '''
    电影类型模型序列化
    '''
    class Meta:
        model = MovieLines
        fields = ('id', 'lines', 'provenance')


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Movie model simple Serializer
    '''
    poster_thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ('url', 'id', 'poster_thumbnail', 'name', 'grade')

    #多对多或外键字段,自定义关系字段序列化方式
    def get_poster_thumbnail(self, obj):
        #数据库中存放的是图片的相对路径，需要转为带域名全路径
        request = self.context.get('request')
        return request.build_absolute_uri(obj.poster_thumbnail.url)


class MovieDetailSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Movie model detail Serializer
    '''
    movie_type = serializers.SerializerMethodField()
    poster_thumbnail = serializers.SerializerMethodField()
    producer_country = serializers.SerializerMethodField()
    language = serializers.SerializerMethodField()
    release_country = serializers.SerializerMethodField()  

    class Meta:
        model = Movie
        fields = ('url', 'id', 'poster_thumbnail', 'name', 'movie_type','director',
                'actor', 'producer_country', 'language', 'release_date', 'release_country',
                'time_length', 'grade', 'synopsis', 'resource')

    #多对多或外键字段,自定义关系字段序列化方式
    def get_movie_type(self, obj):
        li = [item.name for item in obj.movie_type.all()]
        return '/'.join(li)

    def get_producer_country(self, obj):
        li = [item.name for item in obj.producer_country.all()]
        return '/'.join(li)

    def get_poster_thumbnail(self, obj):
        #数据库中存放的是图片的相对路径，需要转为带域名全路径
        request = self.context.get('request')
        return request.build_absolute_uri(obj.poster_thumbnail.url)

    def get_language(self, obj):       
        li = [item.name for item in obj.language.all()]
        return '/'.join(li)

    def get_release_country(self, obj):
        return obj.release_country.name


class BlogTypeCountSerializer(serializers.ModelSerializer):
    '''
    博客类型模型序列化,带统计字段
    '''
    blog_count = serializers.IntegerField()

    class Meta:
        model = BlogType
        fields = ('id', 'name', 'blog_count')
        # exclude = ('id',)
        # fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
    '''
    用户模型序列化
    '''
    class Meta:
        model = User
        fields = ('id', 'username')


class BlogTypeSerializer(serializers.ModelSerializer):
    '''
    博客类型模型序列化
    '''
    class Meta:
        model = BlogType
        fields = ('id', 'name')


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    '''
    博客模型序列化
    '''
    blog_type = BlogTypeSerializer()
    post_by = UserSerializer()
    text = serializers.SerializerMethodField()
    create_time = serializers.SerializerMethodField()
    class Meta:
        model = Blog
        fields = ('url', 'id', 'title', 'text', 'blog_type', 'create_time',
                'modified_time', 'author', 'post_by')


    def get_text(self, obj):
        request = self.context.get('request')
        return html_str_img_build_absolute_uri(request, obj.text)

    def get_create_time(self, obj):
        time = timezone.localtime(obj.create_time)#UTC时间转本地时间
        return time.strftime('%Y-%m-%d %H:%M:%S')
         






