# from django import views
from django.contrib import admin
from django.urls import path
from blog.models import Customer
from blog.views import index, product_detail, customer_list,customer_details
from blog import views
urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:pk>', product_detail, name='product_detail'),
    path('customer-detaiil/<int:customer_id>/',customer_details, name='customer_details'),
    path('customers/', customer_list, name='customer_list'),
    path('customers/<int:customer_id>/edit/', views.customer_edit, name='customer_edit'),
    path('customers/<int:customer_id>/delete/', views.customer_delete, name='customer_delete'),
]
