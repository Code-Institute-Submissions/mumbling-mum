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

class Item(models.Model):
    name = models.CharField(max_length=100)
    # e.g. 'Set of 2 Floral Fabric Baskets'
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    # referencing above Category model e.g. 'Fabric Baskets'
    description = models.TextField()
    # e.g.'Set of 2 stacking floral fabric baskets. Can be used for plants or for storing toiletries, hair accessories, or bits and bobs..
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # e.g. '15.00'
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    # Option to add image as a jpg or a URL.  Image is not a required field.
    sku = models.CharField(max_length=254, null=True, blank=True, editable=False)
    # SKU calculated by the category pk and item pk.
    clearance = models.BooleanField(default=False, editable=False)
    # Added to allow clearance items to maintain their category and SKU.
    original_price = models.DecimalField(max_digits=6, decimal_places=2, editable=False, default=0)
    # When item is flagged for clearance this will be populated with the original price. 
    out_of_stock = models.BooleanField(default=False, editable=False)
    # Admin can flag an item as out of stock

    def __str__(self):
        return self.name