from django.db import models
from allauth.account.models import EmailAddress
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# User must be logged in to view the profile page.
from allauth.account.signals import user_signed_up
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import MemberProfile
from .forms import MemberProfileForm



@receiver(user_signed_up)
def create_member_profile(sender=User, **kwargs):
    print('User signed up!!!')
    MemberProfile.objects.create(
    user = User.objects.get(username=User.username),
    default_phone_number = '',
    default_street_address1 = '',
    default_street_address2 = '',
    default_town_or_city = '',
    default_county = '',
    default_postcode = '',
    default_country = '',
    )
    

@login_required
def member_profile(request):
    """ View to display the members Profile information """
    member_profile = get_object_or_404(MemberProfile, user=request.user)

    if request.method == 'POST':
        form = MemberProfileForm(request.POST, instance=member_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Member profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = MemberProfileForm(instance=member_profile)
    orders = member_profile.orders.all()

    template = 'members/member_profile.html'

    context = {
        'form': form,
        'orders': orders,
        'member_profile_page': True,
        'member': member_profile.user,
        'default_phone_number' : member_profile.default_phone_number,
        'default_street_address1': member_profile.default_street_address1,
        'default_street_address2' : member_profile.default_street_address2,
        'default_town_or_city' : member_profile.default_town_or_city,
        'default_county': member_profile.default_county,
        'default_postcode': member_profile.default_postcode,
        'default_country': member_profile.default_country,
    }
    return render(request, template, context)

# will need to add a view for the order detail later

@login_required
def admin_page(request):
    """ View to display Admin options """ 
    user= request.user
    if user.is_staff:
        # show page
        template = 'members/admin_page.html'
        context = {
            'user':user,
        }
        return render(request, template, context)
    else:
        # redirect to home page
        return redirect(reverse('home'))




