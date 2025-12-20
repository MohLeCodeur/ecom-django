from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.db.models import Sum, Count, Avg
from django.utils import timezone
from datetime import timedelta
from .models import Payment
from orders.models import Order
from products.models import Product
from django.contrib.auth.models import User


class CustomAdminSite(admin.AdminSite):
    site_header = "InnovAfrique Administration"
    site_title = "InnovAfrique Admin"
    index_title = "Tableau de bord"
    
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('dashboard/', self.admin_view(self.dashboard_view), name='dashboard'),
        ]
        return custom_urls + urls
    
    def dashboard_view(self, request):
        """Vue du dashboard avec statistiques"""
        # Période
        today = timezone.now().date()
        last_30_days = today - timedelta(days=30)
        last_7_days = today - timedelta(days=7)
        
        # Statistiques globales
        total_orders = Order.objects.count()
        total_revenue = Order.objects.filter(paid=True).aggregate(
            total=Sum('total_amount'))['total'] or 0
        total_customers = User.objects.filter(orders__isnull=False).distinct().count()
        total_products = Product.objects.count()
        
        # Commandes récentes
        recent_orders = Order.objects.order_by('-created_at')[:10]
        
        # Produits les plus vendus
        top_products = Product.objects.annotate(
            total_sold=Count('orderitem')
        ).order_by('-total_sold')[:5]
        
        # Statistiques mensuelles
        monthly_revenue = Order.objects.filter(
            paid=True,
            created_at__gte=last_30_days
        ).aggregate(total=Sum('total_amount'))['total'] or 0
        
        monthly_orders = Order.objects.filter(
            created_at__gte=last_30_days
        ).count()
        
        # Statistiques hebdomadaires
        weekly_revenue = Order.objects.filter(
            paid=True,
            created_at__gte=last_7_days
        ).aggregate(total=Sum('total_amount'))['total'] or 0
        
        weekly_orders = Order.objects.filter(
            created_at__gte=last_7_days
        ).count()
        
        # Taux de conversion
        paid_orders = Order.objects.filter(paid=True).count()
        conversion_rate = (paid_orders / total_orders * 100) if total_orders > 0 else 0
        
        # Panier moyen
        average_order = Order.objects.filter(paid=True).aggregate(
            avg=Avg('total_amount'))['avg'] or 0
        
        context = {
            'total_orders': total_orders,
            'total_revenue': int(total_revenue),
            'total_customers': total_customers,
            'total_products': total_products,
            'recent_orders': recent_orders,
            'top_products': top_products,
            'monthly_revenue': int(monthly_revenue),
            'monthly_orders': monthly_orders,
            'weekly_revenue': int(weekly_revenue),
            'weekly_orders': weekly_orders,
            'conversion_rate': round(conversion_rate, 2),
            'average_order': int(average_order),
            'paid_orders': paid_orders,
        }
        
        return render(request, 'admin/dashboard.html', context)


# Créer une instance du site admin personnalisé
admin_site = CustomAdminSite(name='custom_admin')


# Admin pour Payment
@admin.register(Payment, site=admin_site)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'payment_method', 'amount', 'status', 'created_at']
    list_filter = ['payment_method', 'status', 'created_at']
    search_fields = ['order__id', 'transaction_id']
    readonly_fields = ['created_at']
    
    fieldsets = (
        ('Informations de paiement', {
            'fields': ('order', 'payment_method', 'amount', 'status')
        }),
        ('Détails de transaction', {
            'fields': ('transaction_id', 'created_at')
        }),
    )
