from django.urls import path
from . import views

urlpatterns = [
    path('', views.member_profile, name='member_profile'),
    path('admin_page/', views.admin_page, name='admin_page'),
    path('order_detail/<int:order_id>', views.order_detail, name='order_detail'),
]
