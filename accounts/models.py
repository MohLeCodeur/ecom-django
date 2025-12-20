from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """Profil utilisateur étendu"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name="Utilisateur")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Téléphone")
    address = models.CharField(max_length=250, blank=True, verbose_name="Adresse")
    city = models.CharField(max_length=100, blank=True, verbose_name="Ville")
    postal_code = models.CharField(max_length=20, blank=True, verbose_name="Code postal")
    country = models.CharField(max_length=100, blank=True, default="Côte d'Ivoire", verbose_name="Pays")
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name="Avatar")
    bio = models.TextField(blank=True, verbose_name="Biographie")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Créé le")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Modifié le")
    
    class Meta:
        verbose_name = "Profil utilisateur"
        verbose_name_plural = "Profils utilisateurs"
    
    def __str__(self):
        return f"Profil de {self.user.username}"
    
    def get_full_address(self):
        """Retourne l'adresse complète"""
        parts = [self.address, self.city, self.postal_code, self.country]
        return ', '.join(filter(None, parts))


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Créer automatiquement un profil lors de la création d'un utilisateur"""
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Sauvegarder le profil lors de la sauvegarde de l'utilisateur"""
    instance.profile.save()
