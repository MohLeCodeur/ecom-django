"""
Script de vérification avant déploiement sur Render
Exécutez : python check_deployment.py
"""

import os
import sys
from pathlib import Path

def check_file_exists(filepath, description):
    """Vérifie qu'un fichier existe"""
    if Path(filepath).exists():
        print(f"✅ {description}")
        return True
    else:
        print(f"❌ {description} - MANQUANT")
        return False

def check_gitignore():
    """Vérifie que .gitignore contient les bonnes entrées"""
    required_entries = ['.env', 'venv/', 'db.sqlite3', '/media', '/staticfiles']
    
    if not Path('.gitignore').exists():
        print("❌ Fichier .gitignore manquant")
        return False
    
    with open('.gitignore', 'r') as f:
        content = f.read()
    
    missing = []
    for entry in required_entries:
        if entry not in content:
            missing.append(entry)
    
    if missing:
        print(f"⚠️  .gitignore incomplet - Manque : {', '.join(missing)}")
        return False
    else:
        print("✅ .gitignore correctement configuré")
        return True

def check_requirements():
    """Vérifie que requirements.txt contient les dépendances nécessaires"""
    required_packages = [
        'Django',
        'gunicorn',
        'psycopg2-binary',
        'whitenoise',
        'dj-database-url',
        'cloudinary',
        'django-cloudinary-storage'
    ]
    
    if not Path('requirements.txt').exists():
        print("❌ requirements.txt manquant")
        return False
    
    with open('requirements.txt', 'r') as f:
        content = f.read()
    
    missing = []
    for package in required_packages:
        if package.lower() not in content.lower():
            missing.append(package)
    
    if missing:
        print(f"⚠️  requirements.txt incomplet - Manque : {', '.join(missing)}")
        return False
    else:
        print("✅ requirements.txt contient toutes les dépendances")
        return True

def main():
    print("\n" + "="*60)
    print("🔍 VÉRIFICATION AVANT DÉPLOIEMENT SUR RENDER")
    print("="*60 + "\n")
    
    checks = []
    
    # Vérifier les fichiers essentiels
    print("📁 Fichiers de configuration :")
    checks.append(check_file_exists('requirements.txt', 'requirements.txt'))
    checks.append(check_file_exists('build.sh', 'build.sh'))
    checks.append(check_file_exists('runtime.txt', 'runtime.txt'))
    checks.append(check_file_exists('render.yaml', 'render.yaml'))
    checks.append(check_file_exists('.env.example', '.env.example'))
    checks.append(check_file_exists('manage.py', 'manage.py'))
    
    print("\n📚 Documentation :")
    checks.append(check_file_exists('README.md', 'README.md'))
    checks.append(check_file_exists('DEPLOIEMENT_RENDER.md', 'Guide de déploiement'))
    checks.append(check_file_exists('MAINTENANCE.md', 'Guide de maintenance'))
    
    print("\n🔧 Configuration :")
    checks.append(check_gitignore())
    checks.append(check_requirements())
    
    # Vérifier la structure Django
    print("\n🏗️  Structure Django :")
    checks.append(check_file_exists('innovafrique/settings.py', 'settings.py'))
    checks.append(check_file_exists('innovafrique/wsgi.py', 'wsgi.py'))
    checks.append(check_file_exists('innovafrique/urls.py', 'urls.py'))
    
    # Résumé
    print("\n" + "="*60)
    total = len(checks)
    passed = sum(checks)
    
    if passed == total:
        print(f"✅ SUCCÈS : {passed}/{total} vérifications passées")
        print("="*60)
        print("\n🚀 Votre projet est prêt pour le déploiement !")
        print("\n📖 Prochaines étapes :")
        print("   1. Lisez DEPLOIEMENT_RENDER.md")
        print("   2. Créez un compte Cloudinary")
        print("   3. Poussez votre code sur GitHub")
        print("   4. Déployez sur Render")
        print("\n" + "="*60 + "\n")
        return 0
    else:
        print(f"⚠️  ATTENTION : {passed}/{total} vérifications passées")
        print("="*60)
        print("\n❌ Corrigez les problèmes ci-dessus avant de déployer.")
        print("\n" + "="*60 + "\n")
        return 1

if __name__ == "__main__":
    sys.exit(main())
