from django.contrib import admin
from django.urls import path
from . import views
from .views import blog_list, blog_detail, like_entry, add_blog_entry

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('blog_detail/<int:blogentry_id>/', views.blog_detail, name='blog_detail'),
    path('like/<int:blogentry_id>/', views.like_entry, name='like_entry'),
    path('add_blog_entry/', views.add_blog_entry, name='add_blog_entry'),
    path('manage_blog/', views.manage_blog, name='manage_blog'),
    path('edit_blog_entry/<int:blogentry_id>', views.edit_blog_entry, name='edit_blog_entry'),
    path('delete_blog_entry/<int:blogentry_id>', views.delete_blog_entry, name='delete_blog_entry'),
]
