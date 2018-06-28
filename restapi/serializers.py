from django.contrib.auth.models import User
from rest_framework import serializers
from movies.models import Language, Country, Movie, MovieType, MovieLines
from blog.models import Blog, BlogType


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
        return obj.poster_thumbnail.name


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
        return obj.poster_thumbnail.name

    def get_language(self, obj):       
        li = [item.name for item in obj.language.all()]
        return '/'.join(li)

    def get_release_country(self, obj):
        return obj.release_country.name


class BlogTypeSerializer(serializers.ModelSerializer):
    '''
    博客类型模型序列化
    '''
    class Meta:
        model = BlogType
        fields = ('id', 'name')



class UserSerializer(serializers.ModelSerializer):
    '''
    用户模型序列化
    '''
    class Meta:
        model = User
        fields = ('id', 'username')



class BlogSerializer(serializers.HyperlinkedModelSerializer):
    '''
    博客模型序列化
    '''
    blog_type = BlogTypeSerializer()
    post_by = UserSerializer()

    class Meta:
        model = Blog
        fields = ('url', 'id', 'title', 'text', 'blog_type', 'create_time',
                'modified_time', 'author', 'post_by')



class BlogTypeSerializer(serializers.ModelSerializer):
    '''
    用户模型序列化
    '''
    class Meta:
        model = BlogType
        fields = ('id', 'name')




