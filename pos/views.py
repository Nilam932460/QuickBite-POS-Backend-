from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MenuItem,Order,OrderItem
from .serializers import MenuItemSerializer,OrderSerializer
from datetime import date, timedelta


class AvailableMenuItemsAPIView(APIView):
    def get(self, request):

        menu_items = MenuItem.objects.filter(availability=True)
        if not menu_items:
            return Response({"message": "No available menu items."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MenuItemSerializer(menu_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class PlaceOrderView(APIView):
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save()  # Save the order and its items
            return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class OrderListView(APIView):
    def get(self, request):
        orders = Order.objects.all()  
        serializer = OrderSerializer(orders, many=True)  
        return Response(serializer.data, status=status.HTTP_200_OK)    
    

class OrderStatusUpdateView(APIView):
    def patch(self, request, order_id):
        try:
            order = Order.objects.get(id=order_id)  # Fetch the order uisng id
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = OrderSerializer(order, data=request.data, partial=True)  # Partial update
        if serializer.is_valid():
            serializer.save()  # Save the updated order
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
        
class AverageWeekdaySalesView(APIView):
    def get(self, request):
        today = date.today() 
        weekday_dates = []  

        current_day = today
        while len(weekday_dates) < 4:
            current_day -= timedelta(days=1)  
            if current_day.weekday() < 5:  
                weekday_dates.append(current_day)
        results = []
        for day in weekday_dates:
            orders = Order.objects.filter(timestamp__date=day, status='completed')
                  
            revenue = sum(
                item.menu_item.price * item.quantity 
                for order in orders
                for item in order.items.all()  
            )
             
            average = revenue / orders.count() if orders.exists() else 0
                
            results.append({
                "date": day,
                "average_sales": round(average, 2)  
            })
        return Response(results, status=status.HTTP_200_OK)