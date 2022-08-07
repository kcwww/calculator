from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',views.login,name='login'),
    
    path('home',views.home,name='home'),
    
    path('signup',views.signup,name='signup'),
    path('signup_detail',views.signup_detail,name='signup_detail'),
    path('logout',views.logout,name='logout'),

    path('delete<int:class_id>',views.delete,name='delete'),

    #정보 수정 관련 URL
    path('modify/<int:pro_id>', views.modify, name='modify'),
    path('modify/userinfo/<int:pro_id>', views.modify_userinfo, name='modify_userinfo'),
    path('modify/password/<int:pro_id>', views.modify_password, name='modify_password'),

    #비회원 로그인 URL
    #path('guest_login/', views.guest_login, name = 'guest_login'),
    #path('guest_home/<int:guest_id>', views.guest_home, name = 'guest_home'),
    #

]
