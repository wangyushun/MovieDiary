from __future__ import absolute_import   #解决命名问题
import os

from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MovieDiaryProj.settings')

app = Celery('MovieDiaryProj')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
#制定celery配置文件
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)  #任务
# app.conf.result_backend = ‘redis://localhost:6379/0’ #结果保持
