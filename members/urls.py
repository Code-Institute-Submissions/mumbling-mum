from django.urls import path
from . import views

urlpatterns = [
    path('my_profile/', views.member_profile, name='member_profile'),
]
