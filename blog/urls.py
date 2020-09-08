from django.contrib import admin
from django.urls import path
from .views import BlogList

urlpatterns = [
    path('', BlogList.as_view(), name='blog_list'),
]
