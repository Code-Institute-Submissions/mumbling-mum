from django.shortcuts import render
from .models import Item, Category

def all_items(request):
    items = Item.objects.all()
    categories = Category.objects.all()
    context = {
        'items': items,
        'categories': categories,
    }
    return render(request, 'items/items.html', context)

def items_by_category(request, cat):
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