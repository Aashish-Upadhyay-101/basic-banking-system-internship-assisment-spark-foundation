from django.urls import path
from . import views

app_name = "bank"

urlpatterns = [
    path("", views.home, name="home"),
    path("customers/", views.customers, name="customers"),
    path("transfer/", views.transfer_balance, name="transfer-balance"),
    path("customer/<int:id>/", views.customer_detail, name="customer-detail"),
]


