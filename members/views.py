from django.db import models
from allauth.account.models import EmailAddress
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
# User must be logged in to view the profile page.
from allauth.account.signals import user_signed_up
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import MemberProfile

@receiver(user_signed_up)

def create_member_profile(sender=User, **kwargs):
    print('User signed up!!!')
    MemberProfile.objects.create(
    user = User.objects.get(username=User.username),
    #default_email_address = EmailAddress
    default_phone_number = '',
    default_street_address1 = '',
    default_street_address2 = '',
    default_town_or_city = '',
    default_postcode = '',
    default_country = '',
    )
    

@login_required
def member_profile(request):
    """ View to display the members Profile information """
    member_profile = get_object_or_404(MemberProfile, user=request.user)

    template = 'members/member_profile.html'

    context = {
        'member': member_profile.user,
        'default_email_address' : member_profile.default_email_address,
        'default_phone_number' : member_profile.default_phone_number,
        'default_street_address1': member_profile.default_street_address1,
        'default_street_address2' : member_profile.default_street_address2,
        'default_town_or_city' : member_profile.default_town_or_city,
        'default_postcode': member_profile.default_postcode,
        'default_country': member_profile.default_country,
    }
    return render(request, template, context)

# will need to add a view for the order detail later
