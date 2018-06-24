from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse
from django.utils import timezone
from . import forms, models


# Create your views here.

def post_comment(request):
    if request.method == 'POST':
        comment_form = forms.CommentForm(request.POST, user=request.user)
        data = {}
        if comment_form.is_valid():
            comment = models.Comment()
            comment.user = comment_form.cleaned_data['user']
            comment.context = comment_form.cleaned_data['comment']
            comment.content_object = comment_form.cleaned_data['content_object']
            comment.save()
            data['status'] = '200 OK'
            data['username'] = comment.user.username
            time = timezone.localtime(comment.create_time)#UTC时间转本地时间
            data['time'] = time.strftime('%Y-%m-%d %H:%M:%S')
            data['context'] = comment.context
        else:
            data['status'] = 'ERROR'
            data['error_text'] = comment_form.errors.as_text()
        return JsonResponse(data)


def on_error(request):
    pass


