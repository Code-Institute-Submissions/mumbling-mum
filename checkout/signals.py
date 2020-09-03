from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem

# the post_save signal will be received
# if it has come from 'OrderLineItem' it will run this. 
@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    print('im running post_save')
    """ Update the order total when a lineitem is updated or created """
    instance.order.update_total()

@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """ Update the order total when a lineitem is deleted """
    instance.order.update_total()

