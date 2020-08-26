from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import Item, Category
from django.contrib.auth.decorators import login_required
from .forms import ItemForm

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

@login_required
def add_item(request):
    """ A view to allow staff to add a new item to the store """
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        print("Hello !!! errors:{{form.errors}}")
        if form.is_valid():
            form.save()
            # add message
            return redirect(reverse('items'))
        # add fail message
    else:
        form = ItemForm()
        context = {
            'form':form,
        }
        return render(request, 'items/add_item.html', context)

@login_required
def edit_item(request, item_id):
    """ A view to allow staff to edit an item to the store """
    item = get_object_or_404(Item, pk=item_id)
    
    if request.method == 'POST':
        form = ItemForm(request.POST or None, request.FILES or None, instance=item)
        print("Hello !!! errors:{{form.errors}}")
        if form.is_valid():
            item = form.save()
            # add message
            return redirect(reverse('items'))
            # add fail message
    else:
        form = ItemForm(instance=item)
        context = {
            'form':form,
            'item' : item,
        }
        return render(request, 'items/edit_item.html', context)

