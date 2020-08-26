from django.shortcuts import render
from .models import Item, Category

# Create your views here.

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
    context = {
        'items': items,
        'categories': categories,
        'cat': cat,
    }
    return render(request, 'items/items.html', context)




