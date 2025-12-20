from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Order(models.Model):
    """Modèle pour les commandes"""
    STATUS_CHOICES = [
        ('pending', 'En attente'),
        ('processing', 'En traitement'),
        ('shipped', 'Expédiée'),
        ('delivered', 'Livrée'),
        ('cancelled', 'Annulée'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', verbose_name="Utilisateur")
    first_name = models.CharField(max_length=100, verbose_name="Prénom")
    last_name = models.CharField(max_length=100, verbose_name="Nom")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Téléphone")
    address = models.CharField(max_length=250, verbose_name="Adresse")
    city = models.CharField(max_length=100, verbose_name="Ville")
    postal_code = models.CharField(max_length=20, verbose_name="Code postal")
    country = models.CharField(max_length=100, verbose_name="Pays")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Créée le")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Modifiée le")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Statut")
    
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Montant total")
    paid = models.BooleanField(default=False, verbose_name="Payée")
    payment_id = models.CharField(max_length=200, blank=True, verbose_name="ID de paiement")
    
    notes = models.TextField(blank=True, verbose_name="Notes")
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Commande"
        verbose_name_plural = "Commandes"
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['status']),
        ]
    
    def __str__(self):
        return f"Commande #{self.id} - {self.user.username}"
    
    def get_total_cost(self):
        """Calculer le coût total de la commande"""
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    """Modèle pour les articles d'une commande"""
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name="Commande")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Produit")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Quantité")
    
    class Meta:
        verbose_name = "Article de commande"
        verbose_name_plural = "Articles de commande"
    
    def __str__(self):
        return f"{self.quantity}x {self.product.name}"
    
    def get_cost(self):
        """Calculer le coût de cet article"""
        return self.price * self.quantity
