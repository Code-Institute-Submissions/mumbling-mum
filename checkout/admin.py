from django.contrib import admin
from .models import Order, OrderLineItem

class OrderLineItemAdminInline(admin.TabularInline):
    # this is to add the line items to the same view in the admin as the order
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,) # from above to display line items on same screen.
    readonly_fields =('order_no', 'date',
                     'delivery_cost', 'order_total', 
                     'grand_total',)

admin.site.register(Order, OrderAdmin)