from __future__ import absolute_import

from django.core.mail import send_mail
from celery import shared_task


@shared_task()
def send_code_by_email(email, code):
        
        # 发送邮件
        ret = send_mail(
            subject='电影日记', #邮件标题
            message='验证码：{code}'.format(code=code),#邮件内容
            from_email='869588058@qq.com', #发件方
            recipient_list=[email], #收件方
            fail_silently=False,
        )
        return ret


