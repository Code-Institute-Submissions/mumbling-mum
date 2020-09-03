from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from items.models import Item
from shopping_bag.contexts import shopping_bag_contents

import stripe

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        shopping_bag = request.session.get('shopping_bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
        }

        order_form = OrderForm(form_data)
        print({order_form})
        if order_form.is_valid():
            order = order_form.save()
            for item_id, quantity in shopping_bag.items():
                try:
                    item = Item.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        item=item,
                        quantity=quantity,
                    )
                    order_line_item.save()
                except Item.DoesNotExist:
                    messages.error(request, (
                        "One of the items in your shopping bag wasn't found in our database."
                        "Please call us for assistance")
                    )
                    order.delete()
                    return redirect(reverse('view_shopping_bag'))
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number] ))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check the information.')

    else:
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
        messages.warning(request, 'Stripe public key is missing.\
            Did you for get to set it in your environment?')

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, template, context)

def checkout_success(request, order_no):
    """
    Handle Successful checkout
    """
    save_info= request.session.get('save_info')
    order = get_object_or_404(Order, order_no=order_no)
    messages.success(request, f'Order successfully processed! \
        Your Order Number is {order_no}. A confirmation \
        email will be sent to {order.email}')
    if 'shopping_bag' in request.session:
        del request,session['shopping_bag']
    
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)