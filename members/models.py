from django.db import models
from django.contrib.auth.models import User
from allauth.account.models import EmailAddress
from django_countries.fields import CountryField


# Create your models here.
# All auth handles login registration etc.. this is for delivery information and previous order info.
class MemberProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # each user can only have one profile thus one to one field, if user is deleted delete profile
    default_email_address = EmailAddress
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_postcode =models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)
    
    def __str__(self):
        return self.user