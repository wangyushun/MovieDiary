from rest_framework import serializers
from movies import models



class MovieTypeListingField(serializers.RelatedField):
    '''
    电影类型字段
    自定义关系字段序列化方式
    '''
    def to_representation(self, value):
        return value.name


class PosterThumbnailListingField(serializers.RelatedField):
    '''
    海报字段
    自定义关系字段序列化方式
    '''
    def to_representation(self, value):
        return value.name


class CountryListingField(serializers.RelatedField):
    '''
    国家/地区字段
    自定义关系字段序列化方式
    '''
    def to_representation(self, value):
        return value.name


class LanguageListingField(serializers.RelatedField):
    '''
    语言字段
    自定义关系字段序列化方式
    '''
    def to_representation(self, value):
        return value.name


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Movie model Serializer
    '''
    poster_thumbnail = PosterThumbnailListingField(read_only=True)

    class Meta:
        model = models.Movie
        fields = ('url', 'id', 'poster_thumbnail', 'name', 'grade')


class MovieDetailSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Movie model detail Serializer
    '''
    movie_type = MovieTypeListingField(read_only=True)
    poster_thumbnail = PosterThumbnailListingField(read_only=True)
    producer_country = CountryListingField(read_only=True)
    language = LanguageListingField(read_only=True)
    release_country = CountryListingField(read_only=True)

    class Meta:
        model = models.Movie
        fields = ('url', 'id', 'poster_thumbnail', 'name', 'movie_type','director',
                'actor', 'producer_country', 'language', 'release_date', 'release_country',
                'time_length', 'grade', 'synopsis')




