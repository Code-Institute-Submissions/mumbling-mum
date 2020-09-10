from django.contrib import admin
from django.urls import path
from . import views
from .views import blog_list, blog_detail, like_entry

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('blog_detail/<int:blogentry_id>/', views.blog_list, name='blog_detail'),
    path('like/<int:blogentry_id>/', views.like_entry, name='like_entry'),

]
