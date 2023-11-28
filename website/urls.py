from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('category/', views.categoryView, name='category'),
    path('product_detail/<int:pk>', views.product_detail, name= 'product_detail'),
    

]
