from django.urls import path
from . import views 
from .views import AvailableMenuItemsAPIView,PlaceOrderView,OrderListView,OrderStatusUpdateView,AverageWeekdaySalesView

urlpatterns = [

    # List all available menu items. 
    path('menu-items/', AvailableMenuItemsAPIView.as_view(), name='available-menu-items'),
    # place an order.
    path('place-order/', PlaceOrderView.as_view(), name='place-order'),
    # list all exiting orders.
    path('orders/', OrderListView.as_view(), name='order-list'),
    # update order status.
    path('orders/<int:order_id>/update-status/', OrderStatusUpdateView.as_view(), name='order-status-update'),
    # avrage sale per day 
    path('average-weekday-sales/', AverageWeekdaySalesView.as_view(), name='average_weekday_sales'),
]