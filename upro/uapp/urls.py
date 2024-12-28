from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('',views.login_user,name='login'),
    path('signup',views.signup,name='signup'),
    path('welcome',views.main,name='main'),
]
