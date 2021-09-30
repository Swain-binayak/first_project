from django.urls import path
from . import views
urlpatterns=[
    path('',views.login_page,name='login'),
    path('home',views.Home,name='home'),
    path('profile',views.Profile,name='profile'),
    path('logout',views.Logout,name='logout'),
    path('register',views.register,name='register'),
    path('post',views.creat_post,name='post')
]
