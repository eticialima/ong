from django.urls import path
from django.core.paginator import Paginator 
from .views import item_list, purchase_item, user_credits, user_purchases

urlpatterns = [
    path('items/', item_list, name='item_list'),
    path('purchase/<int:item_id>/', purchase_item, name='purchase_item'),
    
    path('user-purchases/', user_purchases, name='user_purchases'),
    
    path('user-credits/', user_credits, name='user_credits'),
]
