"""devsns URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    #정보 수정 관련 URL
    path('modify/', views.modify, name='modify'),
    path('modify/userinfo', views.modify_userinfo, name='modify_userinfo'),
    path('modify/password', views.modify_password, name='modify_password'),

    #비회원 로그인 URL
    path('guest_login/', views.guest_login, name = 'guest_login'),
]
