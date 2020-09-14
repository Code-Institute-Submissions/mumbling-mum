from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
# All auth handles login registration etc.. this is for delivery information and previous order info.
class MemberProfile(models.Model):
    """ Model to store default member info to speed up future purchases """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # each user can only have one profile thus one to one field, if user is deleted delete profile
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_postcode =models.CharField(max_length=20, null=True, blank=True)
    default_county = models.CharField(max_length=40, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)
    
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_member_profile(sender, instance, created, **kwargs):
    """ Create or update the user profile """
    if created:
        MemberProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.memberprofile.save()