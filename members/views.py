from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
# User must be logged in to view the profile page.
from .models import MemberProfile

@login_required
def member_profile(request):
    """ View to display the members Profile information """
    member_profile = get_object_or_404(MemberProfile, user=request.user)

    template = 'members/member_profile.html'

    return render(request, template)



# will need to add a view for the order detail later
