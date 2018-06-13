from django.shortcuts import render, redirect, reverse
from . import forms, models


# Create your views here.

def post_comment(request):
    if request.method == 'POST':
        url_from = request.META.get('HTTP_REFERER', reverse('home'))
        comment_form = forms.CommentForm(request.POST, user=request.user)
        if comment_form.is_valid():
            comment = models.Comment()
            comment.user = comment_form.cleaned_data['user']
            comment.context = comment_form.cleaned_data['comment']
            comment.content_object = comment_form.cleaned_data['content_object']
            comment.save()
            return redirect(url_from)
        else:
            return render(request, 'error.html', {'error_text': comment_form.errors.as_text(), 
                                                    'url_from': url_from})

def on_error(request):
    pass


