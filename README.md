# InnovAfrique - E-commerce Platform

Un site e-commerce complet développé avec Django et MySQL pour promouvoir les produits africains innovants.

## Fonctionnalités

- 🛍️ Catalogue de produits avec catégories
- 🛒 Panier d'achat dynamique
- 👤 Authentification et gestion des utilisateurs
- 📦 Gestion des commandes
- 💳 Système de paiement (Stripe)
- 🔍 Recherche et filtres avancés
- 📱 Design responsive
- 🔐 Interface d'administration complète

## Installation

### Prérequis

- Python 3.8+
- MySQL 8.0+
- pip

### Étapes d'installation

1. Cloner le projet
```bash
cd "Ecommerce Django"
```

2. Créer un environnement virtuel
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

3. Installer les dépendances
```bash
pip install -r requirements.txt
```

4. Configurer la base de données MySQL

Créer une base de données MySQL :
```sql
CREATE DATABASE innovafrique CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'innovafrique_user'@'localhost' IDENTIFIED BY 'votre_mot_de_passe';
GRANT ALL PRIVILEGES ON innovafrique.* TO 'innovafrique_user'@'localhost';
FLUSH PRIVILEGES;
```

5. Créer un fichier `.env` à la racine du projet
```env
SECRET_KEY=votre_cle_secrete_django
DEBUG=True
DB_NAME=innovafrique
DB_USER=innovafrique_user
DB_PASSWORD=votre_mot_de_passe
DB_HOST=localhost
DB_PORT=3306
STRIPE_PUBLIC_KEY=votre_cle_publique_stripe
STRIPE_SECRET_KEY=votre_cle_secrete_stripe
```

6. Effectuer les migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

7. Créer un superutilisateur
```bash
python manage.py createsuperuser
```

8. Charger les données de démonstration (optionnel)
```bash
python manage.py loaddata initial_data.json
```

9. Lancer le serveur de développement
```bash
python manage.py runserver
```

Le site sera accessible à l'adresse : http://127.0.0.1:8000/

## Structure du Projet

```
innovafrique/
├── innovafrique/          # Configuration principale
├── products/              # Gestion des produits
├── cart/                  # Panier d'achat
├── orders/                # Gestion des commandes
├── accounts/              # Authentification
├── payments/              # Paiements
├── static/                # Fichiers statiques (CSS, JS, images)
├── media/                 # Fichiers uploadés
└── templates/             # Templates HTML
```

## Utilisation

### Interface Utilisateur
- Accueil : `/`
- Produits : `/products/`
- Panier : `/cart/`
- Commandes : `/orders/`
- Connexion : `/accounts/login/`

### Interface Admin
- Admin : `/admin/`

## Technologies Utilisées

- **Backend** : Django 5.0
- **Base de données** : MySQL 8.0
- **Frontend** : HTML5, CSS3, JavaScript, Bootstrap 5
- **Paiement** : Stripe
- **Authentification** : Django Auth

## Auteur

InnovAfrique - Plateforme e-commerce pour l'innovation africaine

## Licence

MIT License
