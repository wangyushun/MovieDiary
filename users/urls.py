from django.urls import path, include
from . import views

urlpatterns = [
	path('signin/', views.sign_in, name='signin'),#登陆
    path('signout/', views.sign_out, name='signout'),#注销
    path('signup/', views.sign_up, name='signup'),#注册
    path('userinfo/', views.user_info, name='userinfo'),#用户信息
]
    