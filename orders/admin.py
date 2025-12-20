from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    """Inline pour les articles de commande"""
    model = OrderItem
    raw_id_fields = ['product']
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'email', 'status', 'paid', 'total_amount', 'created_at']
    list_filter = ['status', 'paid', 'created_at']
    search_fields = ['id', 'user__username', 'email', 'first_name', 'last_name']
    list_editable = ['status', 'paid']
    inlines = [OrderItemInline]
    
    fieldsets = (
        ('Informations client', {
            'fields': ('user', 'first_name', 'last_name', 'email', 'phone')
        }),
        ('Adresse de livraison', {
            'fields': ('address', 'city', 'postal_code', 'country')
        }),
        ('Statut et paiement', {
            'fields': ('status', 'paid', 'payment_id', 'total_amount')
        }),
        ('Informations supplémentaires', {
            'fields': ('notes',),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ['created_at', 'updated_at']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'price', 'quantity', 'get_cost']
    list_filter = ['order__created_at']
    search_fields = ['order__id', 'product__name']
    
    def get_cost(self, obj):
        return obj.get_cost()
    get_cost.short_description = 'Coût total'
