from django.db import models
from orders.models import Order


class Payment(models.Model):
    """Modèle pour les paiements"""
    PAYMENT_METHOD_CHOICES = [
        ('stripe', 'Stripe'),
        ('paypal', 'PayPal'),
        ('bank_transfer', 'Virement bancaire'),
        ('cash_on_delivery', 'Paiement à la livraison'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'En attente'),
        ('completed', 'Complété'),
        ('failed', 'Échoué'),
        ('refunded', 'Remboursé'),
    ]
    
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment', verbose_name="Commande")
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, verbose_name="Méthode de paiement")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Montant")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Statut")
    
    transaction_id = models.CharField(max_length=200, blank=True, verbose_name="ID de transaction")
    payment_details = models.JSONField(blank=True, null=True, verbose_name="Détails du paiement")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Créé le")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Modifié le")
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Paiement"
        verbose_name_plural = "Paiements"
    
    def __str__(self):
        return f"Paiement #{self.id} - Commande #{self.order.id}"
