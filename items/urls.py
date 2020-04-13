from django.urls import path 
import items.views


#what naming convention do we want to use 
urlpatterns = [path('add',items.views.add_item, name="add_item"),
               path('myItems',items.views.my_items,name="my_items"),
               path('edit/<int:pk>',items.views.edit_item,name="edit_item"),]
               
               