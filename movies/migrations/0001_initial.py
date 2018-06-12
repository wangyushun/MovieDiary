# Generated by Django 2.0.4 on 2018-04-30 07:53

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.ImageField(default='', null=True, upload_to='poster')),
                ('name', models.CharField(max_length=25)),
                ('director', models.CharField(default='', max_length=25)),
                ('actor', models.CharField(default='', max_length=25)),
                ('release_date', models.DateField()),
                ('release_country', models.CharField(max_length=20)),
                ('time_length', models.IntegerField(default=0)),
                ('grade', models.CharField(default=0, max_length=10)),
                ('synopsis', ckeditor_uploader.fields.RichTextUploadingField(default='')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='movies.Language')),
            ],
        ),
        migrations.CreateModel(
            name='MovieType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='movies.MovieType'),
        ),
        migrations.AddField(
            model_name='movie',
            name='producer_country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='movies.Country'),
        ),
    ]
