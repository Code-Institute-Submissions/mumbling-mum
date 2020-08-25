from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=254)
    # e.g. 'fabric_baskets'
    display_name = models.CharField(max_length=254, null=True, blank=True)
    # e.g. 'Fabric Baskets'
    # use dunder str so that it doesn't return a string of random strings
    def __str__(self):
        return self.name
    
    def get_display_name(self):
        return self.display_name
