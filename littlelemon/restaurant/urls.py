from django.contrib import admin 
from django.urls import path 
from .views import sayHello, index, MenuItemsView, SingleMenuItemView
  
urlpatterns = [ 
    # path('', sayHello, name='sayHello'), 
    # path('', index, name='index'),
    path('menu/', MenuItemsView.as_view(), name='menu-list'),
    path('menu/<int:pk>', SingleMenuItemView.as_view(), name='menu-details'),
]