from django.urls import path
from .views import (
    home_view, 
    SalesListView,
    SalesDetailView,
    )
from sales import views

app_name = 'sales'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('sales', SalesListView.as_view(), name='sales'),
    path('sales/<pk>', SalesDetailView.as_view(), name='detail'),
] 