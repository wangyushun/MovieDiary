# Generated by Django 2.0.4 on 2018-06-28 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0018_auto_20180627_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='create_datetime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建日期'),
        ),
    ]
