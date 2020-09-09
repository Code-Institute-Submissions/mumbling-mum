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
        if form.is_valid():
            form.save()
            # Create SKU
            sku1 = str(item.category.pk*10)
            sku2 = str(item.pk*10)
            sku = sku1 + sku2
            print(sku)
            Item.objects.filter(pk=item.pk).update(sku=sku)
            return redirect(reverse('items'))
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
        if form.is_valid():
            item = form.save()
            # update sku - if Category changes
            sku1 = str(item.category.pk*10)
            sku2 = str(item.pk*10)
            sku = sku1 + sku2
            print(sku)
            Item.objects.filter(pk=item.pk).update(sku=sku)
            return redirect(reverse('items'))

    else:
        form = ItemForm(instance=item)
        context = {
            'form':form,
            'item' : item,
        }
        return render(request, 'items/edit_item.html', context)

@login_required
def delete_item(request, item_id):
    """ Delete an item from the store """
    item = get_object_or_404(Item, pk=item_id)
    item.delete()
    return redirect(reverse('items'))

@login_required
def manage_items(request):
    """ View to display All Items and management actions """ 
    user= request.user
    if user.is_staff:
        items = Item.objects.all()
        categories = Category.objects.all()
        template = 'items/manage_items.html'
        context = {
            'user':user,
            'items': items,
            'categories': categories,
        }
        return render(request, template, context)
    else:
        # redirect to home page only Staff can view tha manage items page
        return redirect(reverse('home'))

@login_required
def manage_items_by_category(request, cat):
    """ A view to show items filtered by category """
    user= request.user
    if user.is_staff:
        items = Item.objects.filter(category=cat)
        categories = Category.objects.all()
        template = 'items/manage_items.html'
        filtered = True
        context = {
            'items': items,
            'categories': categories,
            'cat': cat,
            'filtered' : filtered,
        }
        return render(request, template, context)
    else:
        # redirect to home page only Staff can view tha manage items page
        return redirect(reverse('home'))

