from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum, Count, Avg
from django.utils import timezone
from datetime import timedelta
from orders.models import Order
from products.models import Product
from django.contrib.auth.models import User
from .models import Payment
import stripe
import json

# Configuration de Stripe
stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def payment_process(request, order_id):
    """Page de paiement Stripe"""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    if request.method == 'POST':
        try:
            # Créer une session de paiement Stripe
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'xof',  # Franc CFA
                        'unit_amount': int(order.total_amount),  # Montant en centimes
                        'product_data': {
                            'name': f'Commande #{order.id}',
                            'description': f'{order.items.count()} article(s)',
                        },
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url=request.build_absolute_uri(f'/payments/success/{order.id}/'),
                cancel_url=request.build_absolute_uri(f'/payments/cancel/{order.id}/'),
                client_reference_id=str(order.id),
            )
            
            return redirect(checkout_session.url)
            
        except Exception as e:
            messages.error(request, f'Erreur lors du paiement : {str(e)}')
            return redirect('orders:order_detail', order_id=order.id)
    
    context = {
        'order': order,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
    }
    return render(request, 'payments/process.html', context)


@login_required
def payment_success(request, order_id):
    """Page de succès après paiement"""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    # Marquer la commande comme payée
    order.paid = True
    order.save()
    
    # Créer un enregistrement de paiement
    Payment.objects.create(
        order=order,
        payment_method='stripe',
        amount=order.total_amount,
        status='completed',
        transaction_id=f'stripe_{order.id}',
    )
    
    messages.success(request, 'Paiement effectué avec succès !')
    return render(request, 'payments/success.html', {'order': order})


@login_required
def payment_cancel(request, order_id):
    """Page d'annulation de paiement"""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    messages.warning(request, 'Paiement annulé.')
    return render(request, 'payments/cancel.html', {'order': order})


@csrf_exempt
def stripe_webhook(request):
    """Webhook pour recevoir les événements Stripe"""
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        return HttpResponse(status=400)
    
    # Traiter l'événement
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        order_id = session.get('client_reference_id')
        
        if order_id:
            try:
                order = Order.objects.get(id=order_id)
                order.paid = True
                order.save()
                
                Payment.objects.create(
                    order=order,
                    payment_method='stripe',
                    amount=order.total_amount,
                    status='completed',
                    transaction_id=session.get('payment_intent'),
                )
            except Order.DoesNotExist:
                pass
    
    return HttpResponse(status=200)


@staff_member_required
def admin_dashboard(request):
    """Vue du dashboard admin avec statistiques"""
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
