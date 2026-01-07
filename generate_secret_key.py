"""
Script pour générer une nouvelle SECRET_KEY Django
Exécutez : python generate_secret_key.py
"""

from django.core.management.utils import get_random_secret_key

if __name__ == "__main__":
    secret_key = get_random_secret_key()
    print("\n" + "="*60)
    print("🔐 Nouvelle SECRET_KEY générée :")
    print("="*60)
    print(f"\n{secret_key}\n")
    print("="*60)
    print("Copiez cette clé dans votre fichier .env ou dans Render")
    print("="*60 + "\n")
