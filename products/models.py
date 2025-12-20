from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    """Modèle pour les catégories de produits"""
    name = models.CharField(max_length=200, verbose_name="Nom")
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True, verbose_name="Description")
    image = models.ImageField(upload_to='categories/', blank=True, null=True, verbose_name="Image")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Créé le")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Modifié le")
    
    class Meta:
        ordering = ['name']
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('products:product_list_by_category', args=[self.slug])


class Product(models.Model):
    """Modèle pour les produits"""
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name="Catégorie")
    name = models.CharField(max_length=200, verbose_name="Nom")
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(verbose_name="Description")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix")
    stock = models.PositiveIntegerField(default=0, verbose_name="Stock")
    available = models.BooleanField(default=True, verbose_name="Disponible")
    image = models.ImageField(upload_to='products/', verbose_name="Image principale")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Créé le")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Modifié le")
    
    # Champs supplémentaires pour l'e-commerce
    featured = models.BooleanField(default=False, verbose_name="Produit vedette")
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name="Réduction (%)")
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Produit"
        verbose_name_plural = "Produits"
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['available']),
            models.Index(fields=['-created_at']),
        ]
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('products:product_detail', args=[self.slug])
    
    @property
    def discounted_price(self):
        """Calcule le prix après réduction"""
        if self.discount_percentage > 0:
            discount_amount = (self.price * self.discount_percentage) / 100
            final_price = self.price - discount_amount
            return int(final_price)  # Convertir en entier pour un affichage propre
        return int(self.price)
    
    @property
    def is_in_stock(self):
        """Vérifie si le produit est en stock"""
        return self.stock > 0


class ProductImage(models.Model):
    """Modèle pour les images supplémentaires des produits"""
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE, verbose_name="Produit")
    image = models.ImageField(upload_to='products/gallery/', verbose_name="Image")
    alt_text = models.CharField(max_length=200, blank=True, verbose_name="Texte alternatif")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Créé le")
    
    class Meta:
        verbose_name = "Image de produit"
        verbose_name_plural = "Images de produits"
    
    def __str__(self):
        return f"Image pour {self.product.name}"


class Review(models.Model):
    """Modèle pour les avis sur les produits"""
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE, verbose_name="Produit")
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name="Utilisateur")
    rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)], verbose_name="Note")
    comment = models.TextField(verbose_name="Commentaire")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Créé le")
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Avis"
        verbose_name_plural = "Avis"
        unique_together = ['product', 'user']
    
    def __str__(self):
        return f"Avis de {self.user.username} sur {self.product.name}"
