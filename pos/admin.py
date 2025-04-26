from django.contrib import admin
from .models import MenuItem, Order, OrderItem

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'availability']
    list_editable = ['price', 'availability']
    list_filter = ['availability']
    ordering = ['name']
admin.site.register(MenuItem, MenuItemAdmin)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'timestamp', 'status']
    list_filter = ['status']
    inlines = [OrderItemInline]
admin.site.register(Order, OrderAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'menu_item', 'quantity']
    ordering = ['order']
admin.site.register(OrderItem, OrderItemAdmin)

