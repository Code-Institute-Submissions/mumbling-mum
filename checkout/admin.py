from django.contrib import admin
from .models import Order, OrderLineItem

class OrderLineItemAdminInline(admin.TabularInline):
    """ add the line items to the same view in the admin as the order """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)
class OrderAdmin(admin.ModelAdmin):
    """from above to display line items on same screen, 
    declare some fields read only so that they cannot be edited and compromise the order"""
    inlines = (OrderLineItemAdminInline,) 
    readonly_fields =('order_no', 'date',
                     'delivery_cost', 'order_total', 
                     'grand_total', 'original_bag_items',
              'stripe_pid' )
    # declare the fields to maintain the order. 
    fields = ('order_no', 'member_profile', 'date', 'full_name',
              'email', 'phone_number', 'street_address1',
              'street_address2', 'town_or_city', 'county', 
              'postcode', 'country', 'delivery_cost',
              'order_total', 'grand_total', 'original_bag_items',
              'stripe_pid')
    # restrict the columns that show up in the order list to only a few key items
    list_display = ('order_no','date', 'full_name',  
                    'delivery_cost','order_total', 'grand_total',)
    # display the orders so the most recent is at the top
    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)