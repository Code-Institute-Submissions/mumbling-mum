from django.db import models
from django.contrib.auth.models import User
from members.models import MemberProfile
from django.urls import reverse
from datetime import datetime, date

# blog categories
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class BlogEntry(models.Model):
    # create blog db
    title = models.CharField(max_length=255)
    # e.g. 'Code BROWN'
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    # e.g. 'Poo Stories'
    author = models.ForeignKey(MemberProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='blog_entries')
    # Included for future if there are additional blog authors
    post_date = models.DateField(auto_now_add=True)
    body = models.TextField()
    # Actual blog entry
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    # Option to add image as a jpg or a URL.  Image is not a required field.

    def __str__(self):
        return self.title + '|' +  str(self.author)
    
class Comments(models.Model):
    blog_entry = models.ForeignKey('BlogEntry', null=True, blank=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(MemberProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='blog_comments')
    body = models.TextField()

class Likes(models.Model):
    blog_entry = models.ForeignKey('BlogEntry', null=True, blank=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(MemberProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='blog_likes')


    
