from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ("order_number", "customer_name", "status", "total_price", "created_at")
    list_filter = ("status",)
    search_fields = ("order_number", "customer_name")

admin.site.register(Order, OrderAdmin)
