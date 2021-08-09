from django.urls import path 
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('add/',add_employee,name='add'),
    path('edit/<int:id>/',edit_employee,name='edit-employee'),
    path('delete/<int:id>/',delete_employee,name='delete'),
    path('search_employee',search_employee,name='search-employee'),
]