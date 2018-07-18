from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Movie

class AllMoviesRssFeed(Feed):
    # 显示在聚合阅读器上的标题
    title = "电影日记"

    # 通过聚合阅读器跳转到网站的地址
    link = "/movie/"

    # 显示在聚合阅读器上的描述信息
    description = "推荐好电影"

    # 需要显示的内容条目
    def items(self):
        return Movie.objects.order_by('-create_datetime')[:5]

    # 聚合器中显示的内容条目的标题
    def item_title(self, item):
        countrys = [country.name for country in item.producer_country.all()]
        return '[{countrys}] {name}'.format(countrys='/'.join(countrys), name=item.name)


    # 聚合器中显示的内容条目的描述
    def item_description(self, item):
        return item.synopsis

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse('movie_detail', args=[item.pk])

