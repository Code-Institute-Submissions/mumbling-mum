from django.shortcuts import render,redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from shopping_bag.contexts import shopping_bag_contents

import stripe

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    shopping_bag = request.session.get('shopping_bag', {})
    if not shopping_bag:
        messages.error(request, "There's nothing in your shopping bag at the moment")
        return redirect(reverse('items'))

    current_shopping_bag = shopping_bag_contents(request)
    total = current_shopping_bag['grand_total']
    # stripe requires an integer
    stripe_total = round(total * 100)
    # create the payment intent
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    if not stripe_public_key:
        messages.warning(request, 'Strip public key is missing.\
            Did you for get to set it in your environment?')

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, template, context)