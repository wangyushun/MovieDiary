from django import forms
from django.contrib import auth
from django.contrib.auth.models import User

#登陆表单
class SignInForm(forms.Form):
    username = forms.CharField(label='用户名', 
                                max_length=20,
                                widget=forms.TextInput(attrs={
                                                        'class': 'form-control',
                                                        'placeholder': '请输入用户名'}))
    password = forms.CharField(label='密码', 
                                max_length=20,
                                widget=forms.PasswordInput(attrs={
                                                        'class': 'form-control',
                                                        'placeholder': '请输入密码'}))

    def clean(self):
        '''
        在条用is_valid()后会被调用
        '''
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = auth.authenticate(username=username, password=password)#验证用户
        if user is None:
            raise forms.ValidationError('用户名或密码错误')
        else:
            self.cleaned_data['user'] = user
        return self.cleaned_data


class SignUpForm(forms.Form):
    """docstring for SignUpForm"""
    email = forms.CharField(label='邮箱', 
                                max_length=100,
                                widget=forms.EmailInput(attrs={
                                                        'class': 'form-control',
                                                        'placeholder': '请输入邮箱'}))
    username = forms.CharField(label='用户名', 
                                min_length=4,
                                max_length=10,
                                widget=forms.TextInput(attrs={
                                                        'class': 'form-control',
                                                        'placeholder': '请输入用户名'}))
    password = forms.CharField(label='密码', 
                                min_length=5,
                                max_length=16,
                                widget=forms.PasswordInput(attrs={
                                                        'class': 'form-control',
                                                        'placeholder': '请输入密码'}))
    confirm_password = forms.CharField(label='确认密码', 
                                        min_length=5,
                                        max_length=16,
                                        widget=forms.PasswordInput(attrs={
                                                        'class': 'form-control',
                                                        'placeholder': '请再次输入密码'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('邮箱已存在，请重新输入')
        return email
        
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('用户名已存在，请重新输入')
        return username

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if confirm_password != password:
            raise forms.ValidationError('密码输入不一致，请重新输入')
        return password
