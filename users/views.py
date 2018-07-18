import string
from random import sample

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse  
from django.contrib import auth
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
from django.core.mail import send_mail

from . import forms

# Create your views here.
def sign_in(request):
    if request.method == 'POST':
        signin_form = forms.SignInForm(request.POST)
        if signin_form.is_valid():
            user = signin_form.cleaned_data['user']
            if user.is_active:
                auth.login(request, user)
                url = request.session.get('signin_from', reverse('home'))
                return redirect(url, args=[]) 
            signin_form.add_error(None, '用户未激活')
    else: 
        request.session['signin_from'] = request.META.get('HTTP_REFERER', reverse('home'))  #保存登陆前的网页url        
        signin_form = forms.SignInForm()

    content = {}
    content['signin_form'] = signin_form
    return render(request, 'signin.html', content)

@login_required #装饰器作用是要求用户是登陆的状态，用户已登录才会执行被装饰的视图函数
def sign_out(request):
    url = request.META.get('HTTP_REFERER ', reverse('home'))#源网页url
    auth.logout(request)
    return redirect(url, args=[]) 


def sign_up(request):
    if request.method == 'POST':
        signup_form = forms.SignUpForm(request.POST)
        if signup_form.is_valid():
            email = signup_form.cleaned_data['email']
            username = signup_form.cleaned_data['username']
            password = signup_form.cleaned_data['password']
            #创建用户
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            #登陆用户
            user = auth.authenticate(username=username, password=password)#验证用户
            auth.login(request, user)
            url = request.session.get('signup_form', reverse('home'))
            return redirect(url, args=[]) 
    else: 
        request.session['signup_form'] = request.META.get('HTTP_REFERER', reverse('home'))  #保存登陆前的网页url        
        signup_form = forms.SignUpForm()
    content = {}
    content['signup_form'] = signup_form
    return render(request, 'signup.html', content)


@login_required
def user_info(request):
    content = {}
    return render(request, 'user-info.html', content)


@login_required
def change_email(request):      
    if request.method == 'POST':
        email_form = forms.EmailForm(request.POST, request=request)
        if email_form.is_valid():
            user = email_form.cleaned_data['user']
            user.email = email_form.cleaned_data['email']
            user.save()
            return redirect(reverse('userinfo'))
    else:
        email_form = forms.EmailForm()

    content = {}
    content['form_title'] = '更改或绑定邮箱'
    content['submit_text'] = '提交'
    content['action_url'] = reverse('changeemail')
    content['form'] = email_form
    return render(request, 'change_email.html', content)


def send_verify_code(request):
    data = {}
    email = request.GET.get('email', None)
    if not email:
        data['statusCode'] = 400
        data['statusText'] = '400 Bad Request,email is empty'
    else:
        code = ''.join(sample(string.ascii_letters + string.digits, 4))
        request.session['email_verify_code'] = code
        # 发送邮件
        ret = send_mail(
            subject='电影日记', #邮件标题
            message='验证码：{code}'.format(code=code),#邮件内容
            from_email='869588058@qq.com', #发件方
            recipient_list=[email], #收件方
            fail_silently=False,
        )
        if ret == 0:
            data['statusCode'] = 500
            data['statusText'] = '500 Send email faild'
        else:
            data['statusCode'] = 200
            data['statusText'] = '200 OK'
            data['code'] = code
    return JsonResponse(data)






