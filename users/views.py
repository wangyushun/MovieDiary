from django.shortcuts import render, redirect
from django.urls import reverse  
from django.contrib import auth
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User

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


