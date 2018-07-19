from django.urls import path, include
from . import views

urlpatterns = [
    path('signin/', views.sign_in, name='signin'),#登陆
    path('signout/', views.sign_out, name='signout'),#注销
    path('signup/', views.sign_up, name='signup'),#注册
    path('userinfo/', views.user_info, name='userinfo'),#用户信息
    path('change_email/', views.change_email, name='changeemail'),#更改邮箱
    path('verify_code/', views.send_verify_code, name='send_verify_code'),#邮箱验证码
    path('change_password/', views.change_password, name='change_password'),#更改密码
    path('forget_password/', views.forget_password, name='forget_password'),#忘记密码
    path('change_nickname/', views.change_nickname, name='change_nickname'),#更改昵称

]
    