from django.shortcuts import render,redirect, reverse
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    shopping_bag = request.session.get('shopping_bag', {})
    if not shopping_bag:
        messages.error(request, "There's nothing in your shopping bag at the moment")
        return redirect(reverse('items'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HD40YFYmQDcgAXWuHQAxwO7OCu2TzVyQIldUpYL4WwTeiz7XztP1MFkBbNAQVv6N7x1YjbgIrvQAcTvqeNU6DXL00GlY4Zp9e',
        'client_secret': 'test client secret',
    }
    return render(request, template, context)