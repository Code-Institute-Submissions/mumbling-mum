from django.conf import settings
from django.shortcuts import get_object_or_404
from items.models import Item

# to allow all apps to access the shopping bag contents
def shopping_bag_contents(request):

    shopping_bag_items = []
    total = 0
    item_count= 0
    shopping_bag = request.session.get('shopping_bag', {})
    # for each item in the bag get the id so you can get the price. 
    # multiply the price by the quantity and add to the total.
    # add the quantity to the item_count
    for item_id, quantity in shopping_bag.items():
        item = get_object_or_404(Item, pk=item_id)
        total += quantity * item.price
        item_count += quantity
        shopping_bag_items.append({
            'item_id':item_id,
            'quantity':quantity,
            'item':item,
        })


    grand_total = settings.STANDARD_DELIVERY_COST + total
    delivery_cost = settings.STANDARD_DELIVERY_COST

    context = {
        'shopping_bag_items':shopping_bag_items,
        'total':total,
        'item_count':item_count,
        'grand_total': grand_total,
        'delivery_cost': delivery_cost,
    }

    return context