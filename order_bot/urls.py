from django.urls import path 

from . import views  

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("<pk>/order", views.OrderView.as_view(), name="order"),
    path("<pk>/confirm", views.OrderConfirmView.as_view(), name="confirm"),
    path("order_log", views.OrderLogView.as_view(), name="order_log"),
    path("checkout", views.Checkout.as_view(), name="checkout"),
    path("thanks", views.Thanks.as_view(), name="thanks"),
]