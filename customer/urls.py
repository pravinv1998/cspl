from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('addCustomer/', views.addCustomer, name='addCustomer'),
    path('allCustomers/', views.allCustomers, name='allCustomers'),
   
    path('allVisits/', views.allVisits, name='allVisits'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('export/', views.export_users_csv, name='export_users_csv'),
    path('<str:pk>/', views.customer, name='customer'),
    path('delete_customer/<str:pk>/',views.delete_customer, name='delete_customer'),
    
]

