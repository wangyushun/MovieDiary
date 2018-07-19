from django import forms
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

#登陆表单
class SignInForm(forms.Form):
    username = forms.CharField(label='用户名', 
                                max_length=20,
                                widget=forms.TextInput(attrs={
                                                        'class': 'form-control',
                                                        'placeholder': '请输入用户名或邮箱'}))
    password = forms.CharField(label='密码', 
                                max_length=20,
                                widget=forms.PasswordInput(attrs={
                                                        'class': 'form-control',
                                                        'placeholder': '请输入密码'}))

    def clean(self):
        '''
        在调用is_valid()后会被调用
        '''
        username_or_email = self.cleaned_data['username']#输入的可能是用户名或邮箱
        password = self.cleaned_data['password']
        user = auth.authenticate(username=username_or_email, password=password)#验证用户
        if user is None:
            # 输入的可能是邮箱,通过邮箱获得对应的username验证
            try:
                email_user = User.objects.get(email=username_or_email)
            except ObjectDoesNotExist as e:
                pass
            else:
                if email_user:              
                    user = auth.authenticate(username=email_user.username, password=password)#验证用户
                    if user:
                        self.cleaned_data['user'] = user
                        return self.cleaned_data

            raise forms.ValidationError('用户名或密码错误')             
        else:
            self.cleaned_data['user'] = user

        return self.cleaned_data


# 注册表单
class SignUpForm(forms.Form):
    """docstring for SignUpForm"""
    email = forms.CharField(label='邮箱', 
                                max_length=100,
                                widget=forms.EmailInput(attrs={
                                                        'class': 'form-control',
                                                        'placeholder': '请输入邮箱'}))
    verification_code = forms.CharField(label='验证码', 
                                max_length=10,
                                widget=forms.TextInput(attrs={
                                                        'class': 'form-control',
                                                        'placeholder': '请点击“发送验证码”按钮后，输入收到的验证码'}))
    username = forms.CharField(label='用户名', 
                                min_length=4,
                                max_length=10,
                                widget=forms.TextInput(attrs={
                                                        'class': 'form-control',
                                                        'placeholder': '请输入4~10位字母或数字的用户名'}))
    password = forms.CharField(label='密码', 
                                min_length=5,
                                max_length=16,
                                widget=forms.PasswordInput(attrs={
                                                        'class': 'form-control',
                                                        'placeholder': '请输入5~16位字母或数字的密码'}))
    confirm_password = forms.CharField(label='确认密码', 
                                        min_length=5,
                                        max_length=16,
                                        widget=forms.PasswordInput(attrs={
                                                        'class': 'form-control',
                                                        'placeholder': '请再次输入密码'}))
    def __init__(self, *args, **kwargs):
        if 'request' in kwargs:
            self.request = kwargs.pop('request')
        return super(SignUpForm, self).__init__(*args, **kwargs)

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

    def clean_verification_code(self): 
        # 判断验证码是否正确
        code = self.cleaned_data['verification_code']
        email = self.cleaned_data['email']
        if email not in self.request.session:
            raise forms.ValidationError('验证码和邮箱不匹配,请检查邮箱是否有误')

        if (self.request.session.get(email) != code) or (code == ''):
            raise forms.ValidationError('验证码有误')
        return code


#更改邮箱表单
class EmailForm(forms.Form):
    email = forms.EmailField(label='邮箱', 
                                widget=forms.EmailInput(attrs={
                                                        'class': 'form-control',
                                                        'placeholder': '请输入邮箱'}))
    verification_code = forms.CharField(label='验证码', 
                                max_length=10,
                                widget=forms.TextInput(attrs={
                                                        'class': 'form-control',
                                                        'placeholder': '请点击“发送验证码”按钮后，输入收到的验证码'}))

    def __init__(self, *args, **kwargs):
        if 'request' in kwargs:
            self.request = kwargs.pop('request')
        return super(EmailForm, self).__init__(*args, **kwargs)


    def clean(self):
        '''
        在调用is_valid()后会被调用
        '''
        #判断用户是否登陆
        if self.request.user.is_authenticated:
            self.cleaned_data['user'] = self.request.user
        else:
            raise forms.ValidationError('当前用户未登陆')

        return self.cleaned_data

    def  clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('该邮箱已经被绑定')
        return email

    def clean_verification_code(self):
        # 判断验证码是否正确
        code = self.cleaned_data['verification_code']
        email = self.cleaned_data['email']
        if email not in self.request.session:
            raise forms.ValidationError('验证码和邮箱不匹配,请检查邮箱是否有误')
        if (self.request.session.get(email) != code) or (code == ''):
            raise forms.ValidationError('验证码有误')
        return code


#忘记密码表单
class ForgetPasswordForm(forms.Form):
    email = forms.EmailField(label='邮箱', 
                                widget=forms.EmailInput(attrs={
                                                        'class': 'form-control',
                                                        'placeholder': '请输入邮箱'}))
    verification_code = forms.CharField(label='验证码', 
                                max_length=10,
                                widget=forms.TextInput(attrs={
                                                        'class': 'form-control',
                                                        'placeholder': '请点击“发送验证码”按钮后，输入收到的验证码'}))
    username = forms.CharField(label='用户名', 
                                min_length=4,
                                max_length=10,
                                widget=forms.TextInput(attrs={
                                                        'class': 'form-control',
                                                        'placeholder': '请输入4~10位字母或数字的用户名'}))
    new_password = forms.CharField(label='新密码', 
                                min_length=5,
                                max_length=16,
                                widget=forms.PasswordInput(attrs={
                                                        'class': 'form-control',
                                                        'placeholder': '请输入5~16位字母或数字的密码'}))
    new_confirm_password = forms.CharField(label='确认新密码', 
                                        min_length=5,
                                        max_length=16,
                                        widget=forms.PasswordInput(attrs={
                                                        'class': 'form-control',
                                                        'placeholder': '请再次输入密码'}))

    def __init__(self, *args, **kwargs):
        if 'request' in kwargs:
            self.request = kwargs.pop('request')
        return super(ForgetPasswordForm, self).__init__(*args, **kwargs)


    def clean(self):
        '''
        在调用is_valid()后会被调用
        '''
        email = self.cleaned_data['email']
        try:
            user = User.objects.get(email=email)
        except ObjectDoesNotExist:
            raise forms.ValidationError('邮箱对应的用户不存在') 
        else:
            if user.username != self.cleaned_data['username']:
                raise forms.ValidationError('输入的邮箱和用户名不匹配')
            else:
                self.cleaned_data['user'] = user
        return self.cleaned_data

    def clean_email(self):
        email = self.cleaned_data['email']
        return email

    def clean_verification_code(self):
        code = self.cleaned_data['verification_code']
        email = self.cleaned_data['email']
        # 检查邮箱和获取验证码时的邮箱是否一致
        if email not in self.request.session:
            raise forms.ValidationError('邮箱对应验证码不存在,请检查邮箱是否有误')
        # 判断验证码是否正确
        print(self.request.session.get(email), code)
        if (self.request.session.get(email) != code) or (code == ''):
            raise forms.ValidationError('验证码有误')
        return code

    def clean_new_confirm_password(self):
        new_password = self.cleaned_data['new_password']
        new_confirm_password = self.cleaned_data['new_confirm_password']
        if new_password == '' or new_password != new_confirm_password:
            raise forms.ValidationError('输入的密码不一致')
        return new_confirm_password


# 更改密码表单
class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(label='原密码', 
                                min_length=5,
                                max_length=16,
                                widget=forms.PasswordInput(attrs={
                                                        'class': 'form-control',
                                                        'placeholder': '请输入原密码'}))
    new_password = forms.CharField(label='新密码', 
                                min_length=5,
                                max_length=16,
                                widget=forms.PasswordInput(attrs={
                                                        'class': 'form-control',
                                                        'placeholder': '请输入5~16位字母或数字的新密码'}))
    confirm_new_password = forms.CharField(label='确认新密码', 
                                        min_length=5,
                                        max_length=16,
                                        widget=forms.PasswordInput(attrs={
                                                        'class': 'form-control',
                                                        'placeholder': '请再次输入新密码'}))
    def __init__(self, *args, **kwargs):
        if 'request' in kwargs:
            self.request = kwargs.pop('request')
        return super(ChangePasswordForm, self).__init__(*args, **kwargs)
        
    def clean_old_password(self):
        old_password = self.cleaned_data['old_password']
        if not self.request.user.check_password(old_password):
            raise forms.ValidationError('原密码有误')
        return old_password

    def clean_confirm_new_password(self):
        new_password = self.cleaned_data['new_password']
        confirm_new_password = self.cleaned_data['confirm_new_password']
        if confirm_new_password != new_password:
            raise forms.ValidationError('新密码输入不一致，请重新输入')
        return new_password


# 更改密码表单
class ChangeNicknameForm(forms.Form):
    nickname = forms.CharField(label='新昵称', 
                                min_length=1,
                                max_length=16,
                                widget=forms.TextInput(attrs={
                                                        'class': 'form-control',
                                                        'placeholder': '请输入昵称'}))
        
    def clean_nickname(self):
        nickname = self.cleaned_data['nickname']
        if nickname == '':
            raise forms.ValidationError('输入不能为空')
        return nickname

