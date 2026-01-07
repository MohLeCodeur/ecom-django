"""
Script pour créer automatiquement un superutilisateur
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'innovafrique.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Récupérer les credentials depuis les variables d'environnement
username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'admin123')

# Créer le superutilisateur seulement s'il n'existe pas
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f'✅ Superutilisateur "{username}" créé avec succès!')
else:
    print(f'ℹ️  Superutilisateur "{username}" existe déjà.')
