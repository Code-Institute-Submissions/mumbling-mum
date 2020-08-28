from django.conf import settings

# to allow all apps to access the shopping bag contents
def shopping_bag_contents(request):

    shopping_bag_items = []
    total = 0
    product_count= 0

    grand_total = settings.STANDARD_DELIVERY_COST + total

    context = {
        'shopping_bag_items':shopping_bag_items,
        'total':total,
        'product_count':product_count,
        'grand_total': grand_total,
    }

    return context