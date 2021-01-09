from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.xnx, name='about'),
    path('regis', views.regi, name='regis'),
    path('', views.user_login, name='login'),
    path('us_login', views.us_login, name='us_login'),
    path('logout', views.logoutUsers, name='logout'),
    path('register', views.us_regis, name='register'),
    path('home', views.userx, name='home'),
    path('create', views.creat, name='create'),
    path('<int:pk>/newsdetail', views.news_detail.as_view(), name='news-detail'),
    path('<int:pk>/update', views.news_update.as_view(), name='news-update'),
    path('<int:pk>/Delete', views.Delete.as_view(), name='Delete'),

 ]

