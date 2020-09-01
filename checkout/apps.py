from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'

    # import the signals created to receive the post_save and post_delete signals from orderlineitem.
    # see signals.py  
    def ready(self):
        import checkout.signals
