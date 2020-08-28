from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404

# Create your views here.
def view_shopping_bag(request):
    """ A view that renders the shopping bag contents """
    return render(request, 'shopping_bag/shopping_bag.html')

def add_to_shopping_bag(request, item_id):
    """ A view that adds Add the quantity of the specified item to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    #return the user to their previous location on the site
    redirect_url = request.POST.get('redirect_url')
    # store the contents of the shopping bag in the session.
    # check to see if shopping_bag already exists in the session
    # if not create an empty dictionary to hold the shopping bag contents
    shopping_bag = request.session.get('shopping_bag', {})

    
    # if this item already exists in the shopping_bag increase the quantity by above quantity
    if item_id in list(shopping_bag.keys()):
        shopping_bag[item_id] += quantity
    else:
    # otherwise add the item and quantity to the shopping bag dictionary
        shopping_bag[item_id]= quantity
    # update the session shopping_bag with the new contents
    request.session['shopping_bag'] = shopping_bag
    return redirect(redirect_url)

def adjust_shopping_bag(request, item_id):
    """ A view to adjust the quantity of an item in the shopping bag """
    
    quantity = int(request.POST.get('quantity'))
    
    shopping_bag = request.session.get('shopping_bag', {})

    # if the new quantity is less than zero, adjust to the new value
    # else remove the item from the bag
    if quantity > 0:
        shopping_bag[item_id] = quantity
    else:
        shopping_bag.pop(item_id)

    request.session['shopping_bag'] = shopping_bag
    return redirect(reverse(view_shopping_bag))

def remove_from_shopping_bag(request, item_id):
    """ A view to remove an item from the shopping bag"""
    
    shopping_bag = request.session.get('shopping_bag', {})
    shopping_bag.pop(item_id)

    request.session['shopping_bag'] = shopping_bag
    return redirect(reverse(view_shopping_bag))



