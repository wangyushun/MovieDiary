# Generated by Django 2.0.4 on 2018-06-27 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0005_auto_20180614_1241'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-create_time'], 'verbose_name': '评论', 'verbose_name_plural': '评论'},
        ),
    ]