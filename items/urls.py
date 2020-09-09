from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_items, name='items'),
    path('category/<str:cat>/', views.items_by_category, name='items_by_category'),
    path('item_detail/<int:item_id>/', views.item_detail, name='item_detail'),
    path('add_item/', views.add_item, name='add_item'),
    path('edit_item/<int:item_id>/', views.edit_item, name='edit_item'),
    path('delete_item/<int:item_id>/', views.delete_item, name='delete_item'),
    path('manage_items/', views.manage_items, name='manage_items'),
    path('manage_items_by_category/', views.manage_items_by_category, name='manage_items_by_category'),
    path('manage_categories/', views.manage_categories, name='manage_categories'),
    path('add_category/', views.add_category, name='add_category'),
]
