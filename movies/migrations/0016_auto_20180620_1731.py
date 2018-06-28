# Generated by Django 2.0.4 on 2018-06-20 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0015_auto_20180620_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='movie_type',
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_type',
            field=models.ManyToManyField(related_name='movie_type', to='movies.MovieType', verbose_name='电影类型'),
        ),
    ]