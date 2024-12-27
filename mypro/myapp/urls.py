from django.contrib import admin
from django.urls import path
from . import views



urlpatterns=[
   path('',views.index,name='index'),
   path('deletion/<int:id>',views.delete_g,name='deletion'),
   path('edit_g/<int:pk>',views.edit_g,name='edit_g')
]
