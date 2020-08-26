from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_items, name='items'),
    path('category/<str:cat>/', views.items_by_category, name='items_by_category'),
    path('item_detail/<int:item_id>/', views.item_detail, name='item_detail'),
    
]
