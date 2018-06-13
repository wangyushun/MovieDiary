from django import forms
from django.contrib.contenttypes.models import ContentType
from django.db.models import ObjectDoesNotExist 
from django.utils.safestring import mark_safe
from ckeditor.widgets import CKEditorWidget
from lxml.html.clean import clean_html



#评论表单
class CommentForm(forms.Form):
    content_type = forms.CharField(widget=forms.HiddenInput())
    object_id = forms.IntegerField(widget=forms.HiddenInput())
    # comment = forms.CharField(label='欢迎评论', 
    #                             max_length=200,
    #                             widget=forms.Textarea(attrs={
    #                                                     'class': 'form-control',
    #                                                     'placeholder': '评论输入'}))
    comment = forms.CharField(max_length=1000, required=True,
                            widget=CKEditorWidget(config_name='comment_ckeditor',  
                                                attrs={'placeholder': '请输入评论', 
                                                        'class' : 'form-control'}))

    def __init__(self, *args, **kwargs):
        if 'user' in kwargs:
            self.user = kwargs.pop('user')
        super(CommentForm, self).__init__(*args, **kwargs)

    def clean(self):
        '''
        在调用is_valid()后会被调用
        '''
        #检查用户是否登陆
        if not self.user:
            raise forms.ValidationError('未登陆，登陆后可发表评论')
        if self.user.is_authenticated:
            self.cleaned_data['user'] = self.user
        else:
            raise forms.ValidationError('未登陆，登陆后可发表评论')

        #用户评论输入xss安全过滤
        comment = self.cleaned_data['comment']
        comment_new = clean_html(comment)
        self.cleaned_data['comment'] = comment_new

        #获取评论对象
        content_type = self.cleaned_data['content_type']
        object_id = self.cleaned_data['object_id']
        try:
            model_class = ContentType.objects.get(model=content_type).model_class()#模型类名称Movie
            model_obj = model_class.objects.get(pk=object_id)
            self.cleaned_data['content_object'] = model_obj
        except ObjectDoesNotExist:
            raise forms.ValidationError('评论对象不存在')
        return self.cleaned_data

