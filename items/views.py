from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import Item, Category
from django.contrib.auth.decorators import login_required
from .forms import ItemForm, CategoryForm

def all_items(request):
    """ A view to show all items """
    items = Item.objects.all()
    categories = Category.objects.all()
    context = {
        'items': items,
        'categories': categories,
    }
    return render(request,'items/items.html', context)

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
            item=form.save()
            # Create SKU
            sku1 = str(item.category.pk*10)
            sku2 = str(item.pk*10)
            sku = sku1 + sku2
            print(sku)
            Item.objects.filter(pk=item.pk).update(sku=sku)
            return redirect(reverse('manage_items'))
    else:
        form = ItemForm()
        context = {
            'form':form,
        }
        template = 'items/add_item.html'
        return render(request, template, context)

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
            return redirect(reverse('manage_items'))

    else:
        price = item.price
        Item.objects.filter(pk=item.pk).update(original_price = price)
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
    print(item)
    item.delete()
    return redirect(reverse('manage_items'))

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
def manage_items_by_category(request, cat_id):
    """ A view to show items filtered by category """
    user= request.user
    if user.is_staff:
        items = Item.objects.filter(category=cat_id)
        categories = Category.objects.all()
        template = 'items/manage_items.html'
        filtered = True
        context = {
            'items': items,
            'categories': categories,
            'cat_id': cat_id,
            'filtered' : filtered,
        }
        return render(request, template, context)
    else:
        # redirect to home page only Staff can view tha manage items page
        return redirect(reverse('home'))

@login_required
def manage_categories(request):
    """ A view to show items filtered by category """
    user= request.user
    if user.is_staff:
        categories = Category.objects.all()
        template = 'items/manage_categories.html'
        context = {
            'categories': categories,
        }
        return render(request, template, context)
    else:
        # redirect to home page only Staff can view tha manage items page
        return redirect(reverse('home'))

@login_required
def add_category(request):
    """ A view to allow staff to add a new item to the store """
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('manage_categories'))
    else:
        form = CategoryForm()
        context = {
            'form':form,
        }
        template = 'items/add_category.html'
        return render(request, template, context)

@login_required
def edit_category(request, cat_id):
    """ A view to allow staff to edit an item to the store """
    print(cat_id)
    category = get_object_or_404(Category, pk=cat_id)
    print(category)
    if request.method == 'POST':
        form = CategoryForm(request.POST or None, request.FILES or None, instance=category)
        if form.is_valid():
            form.save()
            return redirect(reverse('manage_categories'))

    else:
        form = CategoryForm(instance=category)
        context = {
            'form':form,
            'category' : category,
        }
        return render(request, 'items/edit_category.html', context)

@login_required
def delete_category(request, cat_id):
    """ Delete an item from the store """
    category = get_object_or_404(Category, pk=cat_id)
    category.delete()
    return redirect(reverse('manage_categories'))

def stock_status(request, item_id):
    """ A View to change the stock status """
    item = get_object_or_404(Item, pk=item_id)
    if item.out_of_stock:
        Item.objects.filter(pk=item_id).update(out_of_stock = False)
    else:
        Item.objects.filter(pk=item_id).update(out_of_stock = True)
    return redirect(reverse('manage_items'))
