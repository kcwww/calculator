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

    path('delete<int:comment_id>',views.delete,name='delete'),

]
