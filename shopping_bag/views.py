from django.shortcuts import render

# Create your views here.
def view_shopping_bag(request):
    """ A view that renders the shopping bag contents """
    return render(request, 'shopping_bag/shopping_bag.html')
