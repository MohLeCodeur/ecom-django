# 🎯 InnovAfrique - Guide Complet du Projet E-commerce Django

## 📋 Table des matières
1. [Vue d'ensemble](#vue-densemble)
2. [Installation et Configuration](#installation-et-configuration)
3. [Architecture du Projet](#architecture-du-projet)
4. [Fonctionnalités Détaillées](#fonctionnalités-détaillées)
5. [Utilisation](#utilisation)
6. [Développement](#développement)

---

## 🌟 Vue d'ensemble

**InnovAfrique** est une plateforme e-commerce complète développée avec Django 5.0 et MySQL, conçue pour promouvoir les produits innovants d'Afrique.

### Technologies utilisées
- **Backend** : Django 5.0.1, Python 3.13
- **Base de données** : MySQL (via PyMySQL)
- **Frontend** : Bootstrap 5, Font Awesome 6
- **Paiement** : Stripe (intégration préparée)
- **Images** : Pillow
- **Formulaires** : Django Crispy Forms

---

## 🚀 Installation et Configuration

### Prérequis
- Python 3.8 ou supérieur
- MySQL 8.0 ou supérieur
- pip (gestionnaire de paquets Python)

### Étape 1 : Installation de MySQL

1. Téléchargez MySQL : https://dev.mysql.com/downloads/installer/
2. Installez MySQL Server
3. Notez le mot de passe root

### Étape 2 : Création de la base de données

Ouvrez MySQL et exécutez :
```sql
CREATE DATABASE innovafrique CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'innovafrique_user'@'localhost' IDENTIFIED BY 'innovafrique2024';
GRANT ALL PRIVILEGES ON innovafrique.* TO 'innovafrique_user'@'localhost';
FLUSH PRIVILEGES;
```

**OU** utilisez le script fourni :
```bash
mysql -u root -p < database_setup.sql
```

### Étape 3 : Configuration de l'environnement Python

L'environnement virtuel est déjà créé. Activez-le :
```bash
.\venv\Scripts\activate
```

Les dépendances sont déjà installées. Pour vérifier :
```bash
pip list
```

### Étape 4 : Configuration du fichier .env

Le fichier `.env` est déjà créé avec les paramètres par défaut :
```env
SECRET_KEY=django-insecure-dev-key-change-in-production-abc123xyz789
DEBUG=True
DB_NAME=innovafrique
DB_USER=innovafrique_user
DB_PASSWORD=innovafrique2024
DB_HOST=localhost
DB_PORT=3306
```

**⚠️ Important** : Si vous avez utilisé un mot de passe différent pour MySQL, modifiez `DB_PASSWORD`.

### Étape 5 : Migrations de la base de données

Les migrations sont déjà créées. Appliquez-les :
```bash
python manage.py migrate
```

Vous devriez voir :
```
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying products.0001_initial... OK
  Applying cart.0001_initial... OK
  Applying orders.0001_initial... OK
  Applying accounts.0001_initial... OK
  Applying payments.0001_initial... OK
  ...
```

### Étape 6 : Création du superutilisateur

```bash
python manage.py createsuperuser
```

Entrez :
- Nom d'utilisateur
- Email
- Mot de passe (2 fois)

### Étape 7 : Lancement du serveur

```bash
python manage.py runserver
```

Accédez à :
- **Site** : http://127.0.0.1:8000/
- **Admin** : http://127.0.0.1:8000/admin/

---

## 🏗️ Architecture du Projet

```
Ecommerce Django/
│
├── innovafrique/              # Configuration principale Django
│   ├── settings.py            # Paramètres (DB, apps, middleware)
│   ├── urls.py                # URLs principales
│   ├── wsgi.py                # Configuration WSGI
│   └── asgi.py                # Configuration ASGI
│
├── products/                  # App Produits
│   ├── models.py              # Category, Product, ProductImage, Review
│   ├── views.py               # Liste, détail, recherche, avis
│   ├── admin.py               # Interface admin
│   ├── urls.py                # URLs des produits
│   └── migrations/            # Migrations DB
│
├── cart/                      # App Panier
│   ├── cart.py                # Classe Cart (logique du panier)
│   ├── views.py               # Ajout, suppression, mise à jour
│   ├── context_processors.py # Rendre le panier global
│   └── urls.py                # URLs du panier
│
├── orders/                    # App Commandes
│   ├── models.py              # Order, OrderItem
│   ├── views.py               # Création, liste, détail
│   ├── forms.py               # Formulaire de commande
│   ├── admin.py               # Gestion admin des commandes
│   └── urls.py                # URLs des commandes
│
├── accounts/                  # App Comptes utilisateurs
│   ├── models.py              # UserProfile
│   ├── views.py               # Inscription, connexion, profil
│   ├── forms.py               # Formulaires utilisateur
│   ├── admin.py               # Gestion admin des profils
│   └── urls.py                # URLs des comptes
│
├── payments/                  # App Paiements
│   ├── models.py              # Payment
│   ├── admin.py               # Gestion admin des paiements
│   └── urls.py                # URLs des paiements
│
├── templates/                 # Templates HTML
│   ├── base.html              # Template de base
│   └── products/
│       └── home.html          # Page d'accueil
│
├── static/                    # Fichiers statiques (CSS, JS, images)
├── media/                     # Fichiers uploadés (images produits)
│
├── manage.py                  # Script de gestion Django
├── requirements.txt           # Dépendances Python
├── .env                       # Variables d'environnement
├── .gitignore                 # Fichiers à ignorer par Git
├── database_setup.sql         # Script SQL de création DB
├── README.md                  # Documentation principale
├── QUICKSTART.md              # Guide de démarrage rapide
├── PROJECT_SUMMARY.md         # Résumé du projet
└── COMMANDS.txt               # Commandes utiles
```

---

## 🎯 Fonctionnalités Détaillées

### 1. Gestion des Produits

#### Modèles
- **Category** : Catégories de produits avec images
- **Product** : Produits avec prix, stock, réductions, images
- **ProductImage** : Images supplémentaires pour chaque produit
- **Review** : Avis clients avec notes (1-5 étoiles)

#### Fonctionnalités
- ✅ Catalogue de produits paginé (12 par page)
- ✅ Recherche par nom et description
- ✅ Filtrage par catégorie
- ✅ Tri (prix, nom, date)
- ✅ Produits vedettes
- ✅ Système de réductions (%)
- ✅ Gestion du stock
- ✅ Avis clients (1 par utilisateur par produit)
- ✅ Calcul automatique du prix réduit

### 2. Panier d'Achat

#### Fonctionnalités
- ✅ Ajout de produits au panier
- ✅ Modification des quantités
- ✅ Suppression de produits
- ✅ Vidage complet du panier
- ✅ Vérification automatique du stock
- ✅ Calcul du total
- ✅ Persistance en session
- ✅ Affichage du nombre d'articles dans la navigation

### 3. Commandes

#### Modèles
- **Order** : Commande avec informations client et livraison
- **OrderItem** : Articles de la commande

#### Statuts de commande
- `pending` : En attente
- `processing` : En traitement
- `shipped` : Expédiée
- `delivered` : Livrée
- `cancelled` : Annulée

#### Fonctionnalités
- ✅ Création de commande depuis le panier
- ✅ Pré-remplissage avec les données du profil
- ✅ Mise à jour automatique du stock
- ✅ Historique des commandes
- ✅ Détail de chaque commande
- ✅ Gestion des statuts

### 4. Comptes Utilisateurs

#### Modèles
- **UserProfile** : Extension du modèle User Django

#### Fonctionnalités
- ✅ Inscription avec validation
- ✅ Connexion/Déconnexion
- ✅ Profil utilisateur étendu
- ✅ Avatar
- ✅ Adresse de livraison
- ✅ Création automatique du profil (signals)

### 5. Paiements

#### Modèles
- **Payment** : Paiement lié à une commande

#### Méthodes supportées
- Stripe
- PayPal
- Virement bancaire
- Paiement à la livraison

#### Statuts
- `pending` : En attente
- `completed` : Complété
- `failed` : Échoué
- `refunded` : Remboursé

---

## 📖 Utilisation

### 1. Ajouter des produits (Admin)

1. Connectez-vous à l'admin : http://127.0.0.1:8000/admin/
2. Allez dans **Catégories** → **Ajouter une catégorie**
3. Remplissez le nom (le slug se génère automatiquement)
4. Ajoutez une image (optionnel)
5. Sauvegardez

6. Allez dans **Produits** → **Ajouter un produit**
7. Remplissez les informations :
   - Catégorie
   - Nom
   - Description
   - Prix
   - Stock
   - Image
   - Cochez "Disponible"
   - Cochez "Produit vedette" si souhaité
   - Ajoutez une réduction (%) si souhaité
8. Sauvegardez

### 2. Parcourir le site (Utilisateur)

1. Accédez à http://127.0.0.1:8000/
2. Parcourez les produits vedettes et catégories
3. Cliquez sur "Découvrir nos produits"
4. Utilisez la recherche et les filtres
5. Cliquez sur un produit pour voir les détails

### 3. Passer une commande

1. Ajoutez des produits au panier
2. Cliquez sur l'icône panier
3. Vérifiez votre panier
4. Cliquez sur "Commander"
5. Connectez-vous si nécessaire
6. Remplissez les informations de livraison
7. Validez la commande

### 4. Gérer son profil

1. Connectez-vous
2. Cliquez sur votre nom d'utilisateur
3. Modifiez vos informations
4. Ajoutez un avatar
5. Sauvegardez

---

## 🛠️ Développement

### Créer de nouvelles migrations

Après modification des modèles :
```bash
python manage.py makemigrations
python manage.py migrate
```

### Accéder au shell Django

```bash
python manage.py shell
```

Exemples :
```python
from products.models import Product, Category
from django.contrib.auth.models import User

# Créer une catégorie
cat = Category.objects.create(name="Électronique", slug="electronique")

# Créer un produit
prod = Product.objects.create(
    category=cat,
    name="Smartphone",
    slug="smartphone",
    description="Un super smartphone",
    price=150000,
    stock=10
)

# Lister tous les produits
Product.objects.all()

# Rechercher
Product.objects.filter(name__icontains="phone")
```

### Collecter les fichiers statiques

Pour la production :
```bash
python manage.py collectstatic
```

### Sauvegarder la base de données

```bash
python manage.py dumpdata > backup.json
```

### Restaurer la base de données

```bash
python manage.py loaddata backup.json
```

---

## 🔒 Sécurité

### En développement
- ✅ DEBUG = True
- ✅ SECRET_KEY dans .env
- ✅ ALLOWED_HOSTS = ['*']

### En production (à faire)
- ⚠️ Changer SECRET_KEY
- ⚠️ DEBUG = False
- ⚠️ Définir ALLOWED_HOSTS spécifiquement
- ⚠️ Utiliser HTTPS
- ⚠️ Configurer CSRF_COOKIE_SECURE
- ⚠️ Configurer SESSION_COOKIE_SECURE

---

## 📝 Notes importantes

1. **Stock** : Le stock est automatiquement mis à jour lors de la création d'une commande
2. **Panier** : Le panier est stocké en session (expire après 1 jour)
3. **Images** : Les images sont stockées dans le dossier `media/`
4. **Réductions** : Le prix réduit est calculé automatiquement via `product.discounted_price`
5. **Avis** : Un utilisateur ne peut laisser qu'un seul avis par produit

---

## 🎨 Personnalisation

### Couleurs (dans base.html)
```css
--primary-color: #FF6B35;    /* Orange */
--secondary-color: #004E89;  /* Bleu */
--accent-color: #F7931E;     /* Accent */
--dark-color: #1A1A2E;       /* Sombre */
--light-color: #F5F5F5;      /* Clair */
```

### Pagination
Dans `products/views.py`, ligne 32 :
```python
paginator = Paginator(products, 12)  # Modifier le nombre
```

---

## 🆘 Dépannage

### Erreur de connexion MySQL
```
Access denied for user 'innovafrique_user'@'localhost'
```
**Solution** : Vérifiez le mot de passe dans `.env` et dans MySQL

### Module non trouvé
```
ModuleNotFoundError: No module named 'xxx'
```
**Solution** : 
```bash
.\venv\Scripts\activate
pip install -r requirements.txt
```

### Erreur de migration
```
django.db.utils.OperationalError
```
**Solution** : Vérifiez que MySQL est démarré et que la base de données existe

---

## 📚 Ressources

- [Documentation Django](https://docs.djangoproject.com/)
- [Documentation MySQL](https://dev.mysql.com/doc/)
- [Bootstrap 5](https://getbootstrap.com/docs/5.3/)
- [Font Awesome](https://fontawesome.com/)
- [Stripe API](https://stripe.com/docs)

---

## 🎉 Conclusion

Vous disposez maintenant d'un projet e-commerce Django complet et fonctionnel ! 

**Prochaines étapes suggérées** :
1. Créer les templates manquants
2. Ajouter des produits de démonstration
3. Implémenter le paiement Stripe
4. Personnaliser le design
5. Ajouter des tests
6. Déployer en production

**Bon développement ! 🚀**
