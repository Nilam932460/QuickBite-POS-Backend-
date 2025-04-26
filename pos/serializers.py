from rest_framework import serializers
from .models import MenuItem, OrderItem, Order

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    menu_item = serializers.PrimaryKeyRelatedField(queryset=MenuItem.objects.all())  # Use PK for menu_item

    class Meta:
        model = OrderItem
        fields = ['menu_item', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)  # Nested serializer for related order items

    class Meta:
        model = Order
        fields = ['id', 'timestamp', 'status', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        
        for item_data in items_data:
            menu_item = item_data['menu_item']
            if not menu_item.availability:  # Check if the menu item is unavailable
                raise serializers.ValidationError(f"Menu item '{menu_item.name}' is unavailable.")

        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order
    

    def update(self, instance, validated_data):
        """ Handle partial update of order status. """
        status = validated_data.get('status', None)
        if status:
            instance.status = status  # Update the status field
            instance.save()
        return instance    
    
