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
    category = models.ForeignKey('Category', null=True, blank=False, on_delete=models.SET_NULL)
    # e.g. 'Poo Stories'
    author= models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False, editable=False)
    # author = models.ForeignKey(MemberProfile, on_delete=models.SET_NULL, null=True, blank=False, related_name='blog_entries',editable=False)
    # Included for future if there are additional blog authors
    post_date = models.DateField(auto_now_add=True)
    body = models.TextField()
    # Actual blog entry
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    # Option to add image as a jpg or a URL.  Image is not a required field.
    likes = models.ManyToManyField(User, related_name='blog_entry', editable=False)
    # logs which users have liked the post
    
    def total_likes(self):
        # calculates likes for each blog entry 
        return self.likes.count()


    def __str__(self):
        return self.title + '|' +  str(self.author)
    
class Comment(models.Model):
    blog_entry = models.ForeignKey('BlogEntry', null=True, blank=False, on_delete=models.SET_NULL, editable=False)
    author= models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False, editable=False)
    # author = models.ForeignKey(MemberProfile, on_delete=models.SET_NULL, null=True, blank=False, related_name='blog_comments', editable=False)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)

