from django.contrib import admin
from django.urls import path
from accounts import views
from calapp import views as cal_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',views.login,name='login'),
    
    path('home',views.home,name='home'),
    
    path('signup',views.signup,name='signup'),
    path('signup_detail',views.signup_detail,name='signup_detail'),
    path('logout',views.logout,name='logout'),

    path('delete_all',views.delete_all,name='delete_all'),
    path('delete<int:class_id>',views.delete,name='delete'),

    
    #정보 수정 관련 URL
    path('modify/', views.modify, name='modify'),
    path('modify/userinfo', views.modify_userinfo, name='modify_userinfo'),
    path('modify/password', views.modify_password, name='modify_password'),


    
    path('calculator',cal_views.calculator, name='calculator'),
    #path('class_delete<int:class_id>',cal_views.class_delete,name='class_delete'),
]