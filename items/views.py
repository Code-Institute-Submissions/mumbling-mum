from django.shortcuts import render, get_object_or_404
from .models import Item, Category

def all_items(request):
    """ A view to show all items """
    items = Item.objects.all()
    categories = Category.objects.all()
    context = {
        'items': items,
        'categories': categories,
    }
    return render(request, 'items/items.html', context)

def items_by_category(request, cat):
    """ A view to show items filtered by category """
    items = Item.objects.filter(category=cat)
    categories = Category.objects.all()
    filtered = True
    context = {
        'items': items,
        'categories': categories,
        'cat': cat,
        'filtered' : filtered,
    }
    return render(request, 'items/items.html', context)

def item_detail(request, item_id):
    """ A view to show individual item details """ 
    item = get_object_or_404(Item, pk=item_id)
    context = {
        'item' : item,
    }
    return render(request, 'items/item_detail.html', context)
    

