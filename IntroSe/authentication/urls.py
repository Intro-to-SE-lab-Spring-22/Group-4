from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path('del_auth', views.del_auth, name="del_auth"),
    path('del_user', views.del_user, name="del_user"),
    path('post', views.post, name="post"),
    path('save_post', views.save_post, name="save_post")


]