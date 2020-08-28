from django.shortcuts import render, redirect

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
