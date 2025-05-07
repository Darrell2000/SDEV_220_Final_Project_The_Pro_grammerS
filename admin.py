from django.contrib import admin
from .models import Customer, FoodItem, Order

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'address')
    search_fields = ('name', 'email', 'phone')

@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'meat', 'price')
    list_filter = ('name', 'meat')
    search_fields = ('name', 'meat')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'timestamp')
    list_filter = ('timestamp',)
    date_hierarchy = 'timestamp'
    