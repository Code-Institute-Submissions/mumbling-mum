import uuid

from django.db import models
from members.models import MemberProfile
from items.models import Item
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

# Create your models here.
class Order(models.Model):
    # order no generated at time of order creation. See below
    # It is required and cannot be edited.
    order_no = models.CharField(max_length=32, null=False, editable=False)
    # link to member_profile
    member_profile = models.ForeignKey(MemberProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 =models.CharField(max_length=80, null=False, blank=False)
    town_or_city = models.CharField(max_length=50, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=False, blank=False)
    county = models.CharField(max_length=80, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, default=0)
    order_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, default=0)
    grand_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, default=0)
    original_bag_items = models.TextField(null=False,blank=False,default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def _generate_order_no(self):
        # Generate Order number using UUID
        # random string of 32 characters
        return uuid.uuid4().hex.upper()
    
    def update_total(self):

        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        # Aggregate - the value of multiple rows is grouped together to form a single summary value.
        self.delivery_cost = settings.STANDARD_DELIVERY_COST
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    
    def save(self, *args, **kwargs):
        # Override the original save method to set the order number if it hasn't already been set.
        if not self.order_no:
            self.order_no = self._generate_order_no()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.order_no

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name = 'lineitems')
    item = models.ForeignKey(Item, null=False, blank=False, on_delete=models.CASCADE)
    quantity =  models.IntegerField(null=False, blank=False, default=0)
    # line item total is not editable as it is automatically calculated when the line items is saved.
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        # Override the original save method to set the line item total.
        self.lineitem_total = self.item.price * self.quantity
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'Item {self.item.name} on order {self.order.order_no}'