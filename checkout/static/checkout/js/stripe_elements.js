// get stripe public key and client secret and remove quotation marks
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);

// Create a variable using the stripe public key
var stripe = Stripe(stripePublicKey);

// create an instance of stripe elements
var elements = stripe.elements();

// style the card element
var style = {
    base: {
        color: '#32325d',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#fa755a',
        iconColor: '#fa755a'
    }
};
// Use above to create a card element
var card = elements.create('card', {
    style: style
});

// mount the card element to the div in checkout html
card.mount('#card-element');

// add listener event to check for any errors
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html =
            `<span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span> ${event.error.message}</span>`;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Submit the payment to stripe 
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    //  disable the card element and the submit button to prevent multiple submissions
    card.update({
        'disabled':
        true
    });

    $('#submit-button').attr('disabled', true)

    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function (result) {
        if (result.error) {
            var html =
            `<span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span> ${event.error.message}</span>`;
            $(errorDiv).html(html);
            //  Enable card element and the submit button to allow user to reenter data.
            card.update({
                'disabled':
                false
            });
            $('#submit-button').attr('disabled', false)
        } else {
            // The payment has been processed!
            if (result.paymentIntent.status === 'succeeded') {
               form.submit();
            }
        }
    });
});