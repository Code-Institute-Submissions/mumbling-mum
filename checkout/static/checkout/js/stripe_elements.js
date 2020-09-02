// get stripe public key and client secret and remove quotation marks
var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);

// Create a variable using the stripe public key
var stripe = Stripe(stripe_public_key);

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
var card = elements.create('card', {style: style});

// mount the card element to the div in checkout html
card.mount('#card-element');
